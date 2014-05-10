from browserstack.browserstack import BrowserStack

# BrowserStack API object: Accepts two params, username and access key
# Returns the main API object.
bs = BrowserStack('ashishdubey2', 'p98rYA82bmbANaoGhutL')

# Returns the browsers list as a Python dict.
print 'Browsers: %s' % bs.list_browsers()

# Returns the browsers list as an Python list.
bs.list_browsers(flat=True)

# Create a worker: Accepts required params (os, os_version, and url)
# Optional params can be set using kwargs
# Returns a Worker object
worker = bs.create_worker('ios', '6.0', url='https://github.com/404')

# Returns the list of Worker objects created.
print 'Workers: %s' % bs.list_workers()

# Takes the screenshot and sends the URL in JSON
# This returns an error if the worker is not in "running" state.
worker.get_screenshot('json')
