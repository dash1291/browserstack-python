# browserstack-python
Python wrapper for BrowserStack REST API.

## Usage

### Listing browsers
```python
from browserstack.browserstack import BrowserStack

bs = BrowserStack('someusername', 'userpassword')
print 'Browsers: %s' % bs.list_browsers()
```

### Taking a page screenshot
```python
from browserstack.browserstack import BrowserStack

bs = BrowserStack('someusername', 'userpassword')
worker = bs.create_worker('ios', '6.0', url='https://github.com/404')
res = worker.get_screenshot('json')
```
