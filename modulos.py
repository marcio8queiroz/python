import requests
import http.client
import math
import matematica 
# from matematica import somar


response = requests.get('https://docs.python.org')
print(response.status_code, response.reason)


host = "docs.python.org"
conn = http.client.HTTPSConnection(host)
conn.request("GET", "/3/", headers={"Host": host})
response = conn.getresponse()
print(response.status, response.reason)




v1 = 45
v2 = 36
print (matematica.somar(v1, v2))

print(math.sqrt(v2))

print(chr(8364))