Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 

>>> import urllib
>>> import urllib2
>>> 
>>> url = 'http://www.server.com/login'
>>> user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows Nt)'
>>> values = {'username' : 'ds',  'password' : '121299' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, data, headers)
>>> response = urllib2.urlopen(request)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    response = urllib2.urlopen(request)
  File "C:\Python27\lib\urllib2.py", line 154, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python27\lib\urllib2.py", line 429, in open
    response = self._open(req, data)
  File "C:\Python27\lib\urllib2.py", line 447, in _open
    '_open', req)
  File "C:\Python27\lib\urllib2.py", line 407, in _call_chain
    result = func(*args)
  File "C:\Python27\lib\urllib2.py", line 1228, in http_open
    return self.do_open(httplib.HTTPConnection, req)
  File "C:\Python27\lib\urllib2.py", line 1198, in do_open
    raise URLError(err)
URLError: <urlopen error [Errno 10060] >









>>> page = response.read()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    page = response.read()
NameError: name 'response' is not defined
>>> 
