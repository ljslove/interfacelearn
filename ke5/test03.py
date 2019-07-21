#给头部添加参数
import requests
import urllib3
urllib3.disable_warnings()



#头部的参数是字典格式，然后赋值给headers

h={"connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Accept":"*/*",
    "Accept-Language": "zh-CN,zh;q=0.9"}
r=requests.get("https://api.github.com/events",verify=False,headers=h)

#打印响应的头部
print(r.headers)