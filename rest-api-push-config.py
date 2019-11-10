import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'content-type' : 'application/xml' }
authuser = 'root'
authpwd = 'Juniper'

payload = ("<lock-configuration/><load-configuration><configuration><system><login><message>welcome to REST demo</message></login></system></configuration></load-configuration><commit/><unlock-configuration/>")

url = 'http://192.168.56.151:3000/rpc'

q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload)

print (q.status_code)
