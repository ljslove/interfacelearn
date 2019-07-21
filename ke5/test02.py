#给URL添加参数
import  requests
import urllib3

urllib3.disable_warnings()


#给URL添加参数
par={"key1":"value1","key2":"vlaue2"}

r=requests.get("https://api.github.com/events",verify=False,params=par)

#打印请求的url
print(r.url)

#打印响应的json
print(r.json())

#查看返回的编码格式
print(r.encoding)

