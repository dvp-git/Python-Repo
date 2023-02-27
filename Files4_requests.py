####################
# I/O, streams, and requests
####################

# import io
# stream = io.StringIO()
# stream.write('Learning Python akndasd\n')
# print('Become a Python ninja!',file=stream)
# contents = stream.getvalue()
# print(contents)
# stream.close()

# import io
# with io.StringIO() as stream:
#     stream.write('Learning Python akndasd\n')
#     print('Become a Python ninja!',file=stream)
#     contents = stream.getvalue()
#     print(contents)


# Making HTTP requests
from pprint import pprint 
import requests
urls = {
    "get" :"https://httpbin.org/get?t=learn+python+programming",
    "headers":"https://httpbin.org/headers",
    "ip": "https://httpbin.org/ip",
    "user-agent":"https://httpbin.org/user-agent",
    "UUID":"https://httpbin.org/uuid",
    "JSON":"https://httpbin.org/json",
}

def get_content(title, url):
    resp = requests.get(url) 
    print("Response class {} ".format(type(resp)))   # <class 'requests.models.Response'>
    print("Response for {}".format(title))
    pprint(resp.json())  # resp.text() and then decoder using json.loads() 

for title,url in urls.items():
    get_content(title,url)
    pprint("-" * 40)

# Response class <class 'requests.models.Response'> 
# Response for get
# {'args': {'t': 'learn python programming'},
#  'headers': {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate',
#              'Host': 'httpbin.org',
#              'User-Agent': 'python-requests/2.28.1',
#              'X-Amzn-Trace-Id': 'Root=1-63adbf72-7168e62a55e95dde1edb5ec7'},
#  'origin': '98.11.167.187',
#  'url': 'https://httpbin.org/get?t=learn+python+programming'}
# '----------------------------------------'
# Response class <class 'requests.models.Response'> 
# Response for headers
# {'headers': {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate',
#              'Host': 'httpbin.org',
#              'User-Agent': 'python-requests/2.28.1',
#              'X-Amzn-Trace-Id': 'Root=1-63adbf72-4b3c7af2081c3cb230d4c6fb'}}
# '----------------------------------------'
# Response class <class 'requests.models.Response'> 
# Response for ip
# {'origin': '98.11.167.187'}
# '----------------------------------------'
# Response class <class 'requests.models.Response'> 
# Response for user-agent
# {'user-agent': 'python-requests/2.28.1'}
# '----------------------------------------'
# Response class <class 'requests.models.Response'> 
# Response for UUID
# {'uuid': '41d0642d-0006-4cd7-967c-100bf0d7d65d'}
# '----------------------------------------'
# Response class <class 'requests.models.Response'> 
# Response for JSON
# {'slideshow': {'author': 'Yours Truly',
#                'date': 'date of publication',
#                'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'},
#                           {'items': ['Why <em>WonderWidgets</em> are great',
#                                      'Who <em>buys</em> WonderWidgets'],
#                            'title': 'Overview',
#                            'type': 'all'}],
#                'title': 'Sample Slide Show'}}

url = 'https://httpbin.org/post'
data = dict(title='Learn Python Programming')
resp = requests.post(url, data=data)
pprint('Response for POST')
pprint(resp.json())

'Response for POST'
# {'args': {},
#  'data': '',
#  'files': {},
#  'form': {'title': 'Learn Python Programming'},
#  'headers': {'Accept': '*/*',
#              'Accept-Encoding': 'gzip, deflate',
#              'Content-Length': '30',
#              'Content-Type': 'application/x-www-form-urlencoded',
#              'Host': 'httpbin.org',
#              'User-Agent': 'python-requests/2.28.1',
#              'X-Amzn-Trace-Id': 'Root=1-63adc32f-550099df72cdb6115701afbb'},
#  'json': None,
#  'origin': '98.11.167.187',
#  'url': 'https://httpbin.org/post'}