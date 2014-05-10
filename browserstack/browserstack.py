import json

import requests
from requests.auth import HTTPBasicAuth


class APIException(Exception):
    def __init__(self, code, short_msg, response_dump=None):
        self.message = 'Server returned error %s. %s.' % (code, short_msg)

        if response_dump:
            self.message += 'Response dump:\n%s' % response_dump


def _send_request(url, auth, method='GET', data=None):
    if method == 'GET':
        r = requests.get(url, auth=auth)
    elif method == 'POST':
        r = requests.post(url, auth=auth, data=data)
    elif method == 'DELETE':
        r = requests.delete(url, auth=auth)

    if r.status_code == 200:
        return json.loads(r.text)
    else:
        _handle_errors(r)
        return None


def _handle_errors(response):
    if response.status_code == 401:
        raise APIException(401, 'Auth failed.')

    elif response.status_code == 422:
        raise(APIException(422, 'Invalid request', response.text))


class Worker():
    def __init__(self, base, worker_id):
        self.base = base
        self.worker_url = base.base_url + '/worker/%s' % worker_id

    def get_status(self):
        return _send_request(self.worker_url, self.base.auth)

    def get_screenshot(self, format):
        url = self.worker_url + '/screenshot.%s' % format
        return _send_request(url, self.base.auth)

    def terminate(self):
        url = self.worker_url
        return _send_request(url, self.base.auth, 'DELETE')


class BrowserStack():
    def __init__(self, username, access_key, version=3):
        self.base_url = 'http://api.browserstack.com/%s' % version
        self.username = username
        self.access_key = access_key
        self.auth = HTTPBasicAuth(self.username, self.access_key)

    def api_status(self):
        url = self.base_url + '/status'
        return _send_request(url, self.auth)

    def list_browsers(self, flat=False):
        url = self.base_url + '/browsers'

        if flat:
            url += '?flat=true'

        return _send_request(url, self.auth)

    def create_worker(self, os, os_version, **kwargs):
        url = self.base_url + '/worker'

        post_data = {
            'os': os,
            'os_version': os_version
        }

        other_params = ['browser', 'device', 'browser_version', 'timeout',
            'url', 'name', 'build', 'project']

        for param in other_params:
            if param in kwargs:
                post_data[param] = kwargs[param]


        res = _send_request(url, self.auth, 'POST', post_data)

        if res:
            return Worker(self, res['id'])
        else:
            return None

    def list_workers(self):
        url = self.base_url + '/workers'

        workers = []
        res = _send_request(url, self.auth)

        for w in res:
            workers.append(Worker(self, w['id']))

        return workers
