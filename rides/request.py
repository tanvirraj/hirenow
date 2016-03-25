import urllib2



# import requests
# import json
#
# url = 'http://127.0.0.1:8000/auth/login'
# data = {'username:toha','password:tohatoha'}
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# password_mgr.add_password(None, top_level_url, 'toha', 'tohatoha')
# handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# headers = {'Content-Type': 'application/json', 'Authorization': 'Token 3d06342bde2f0dbf524da181633991c6ae63f027'}
# opener = urllib2.build_opener(urllib2.HTTPHandler, handler)
# request = urllib2.Request(url)
# r = requests.post(url, data=json.dumps(data), headers=headers)


import requests
import json

url = 'http://127.0.0.1:8000/taxilocation/driver_response/'
data = [{ "id": 1,
    "driver": 5,
    "lat": 22.22,
    "lon": 23.25 }]
headers = {'Content-Type': 'application/json'}

r = requests.post(url, data=json.dumps(data), headers=headers)

#
# data2 = { "id": 3,
#     "driver": 5,
#     "lat": 22.22,
#     "lon": 23.25 }
#
#
# r = requests.post(url, data=json.dumps(data2), headers=headers)
#


#
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
#
#
# top_level_url = "http://127.0.0.1:8000/auth/login"
# password_mgr.add_password(None, top_level_url, 'toha', 'tohatoha')
# handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# opener = urllib2.build_opener(urllib2.HTTPHandler, handler)
# request = urllib2.Request(url)
#
#





# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib2.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib2.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib2.install_opener(opener)
# urllib2.urlopen('http://www.example.com/login.html')