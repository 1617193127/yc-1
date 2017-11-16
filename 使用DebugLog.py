Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> httpHandler = urllib2.HTTPHandler(debuglevel=1)
>>> httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
>>> opener = urllib2.build_opener(httpHandler, httpsHandler)
>>> urllib2.install_opener(opener)
>>> response = urllib2.urlopen('http://www.baidu.com')
send: 'GET / HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: www.baidu.com\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Date: Thu, 16 Nov 2017 06:16:33 GMT
header: Content-Type: text/html; charset=utf-8
header: Transfer-Encoding: chunked
header: Connection: Close
header: Vary: Accept-Encoding
header: Set-Cookie: BAIDUID=12B6E350257BEB6B9F1D7556FCF5F0A1:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BIDUPSID=12B6E350257BEB6B9F1D7556FCF5F0A1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: PSTM=1510812993; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BDSVRTM=0; path=/
header: Set-Cookie: BD_HOME=0; path=/
header: Set-Cookie: H_PS_PSSID=24754_1436_24869_21103_24879_20718; path=/; domain=.baidu.com
header: P3P: CP=" OTI DSP COR IVA OUR IND COM "
header: Cache-Control: private
header: Cxy_all: baidu+65f82030f8f88b3a26b12f3af400c572
header: Expires: Thu, 16 Nov 2017 06:15:55 GMT
header: X-Powered-By: HPHP
header: Server: BWS/1.1
header: X-UA-Compatible: IE=Edge,chrome=1
header: BDPAGETYPE: 1
header: BDQID: 0x83779e2500052fcd
header: BDUSERID: 0
>>> 
