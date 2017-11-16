Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> request = urllib2.Request(uri, data=data)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    request = urllib2.Request(uri, data=data)
NameError: name 'uri' is not defined
>>> request = urllib2.Request(baidu, data=data)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    request = urllib2.Request(baidu, data=data)
NameError: name 'baidu' is not defined
>>> request = urllib2.Request(www.baidu.com, data=data)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    request = urllib2.Request(www.baidu.com, data=data)
NameError: name 'www' is not defined
>>> request.get_method = lambda: 'PUT' # or 'DELETE'

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    request.get_method = lambda: 'PUT' # or 'DELETE'
NameError: name 'request' is not defined
>>> response = urllib2.urlopen(request)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    response = urllib2.urlopen(request)
NameError: name 'request' is not defined
>>> 
