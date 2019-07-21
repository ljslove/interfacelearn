import requests
import urllib3
urllib3.disable_warnings()  #忽略https的warnings

#SSLError, ssl都是证书有关的，可以在get中加上verify=false
r=requests.get("https://api.github.com/events",verify=False)

#查看返回的text，如果返回的是text
print(r.text)
#查看返回的状态码
print(r.status_code)

#查看返回的json
print(r.json())

