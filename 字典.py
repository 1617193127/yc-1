Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'yc':1617193127}
>>> dict1
{'yc': 1617193127}
>>> dict1['yc']
1617193127
>>> dict1['yc']=161719366
>>> dict1
{'yc': 161719366}
>>> del dict1['yc']
>>> dict1
{}
>>> users = {
	'A':{
	'diest':'ye',
	'last':'ke',
	'location':'shan',
	},
	'B':{
	'dirst':'liu',
	'last':'ke',
	'location':'shan',
	},
}
>>> for username, userinfo in users.items():
	print("userid: " + username)
	print("userinfo:" + str(userinfo))

	
userid: A
userinfo:{'last': 'ke', 'location': 'shan', 'diest': 'ye'}
userid: B
userinfo:{'last': 'ke', 'dirst': 'liu', 'location': 'shan'}
>>> dict = {'Name':'Zare', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dict.keys():
	print dict[key]

	
7
Zare
>>> 



