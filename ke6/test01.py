#一个基本的post请求

import requests
import urllib3
urllib3.disable_warnings()

#给post添加body参数，参数格式是data

body={
      "key1":"value1",
      "key2":"value2"
}

r=requests.post("http://httpbin.org/post",verify=False,data=body)

#打印响应体
print(r.text)