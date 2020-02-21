import requests
import base64

url= "http://123.206.87.240:8002/web6/"#链接
req= requests.Session()#建立会话
res=req.get(url)#请求网页
flag = res.headers['flag']#header里面搜索flag的报头信息
txt1 = str(base64.b64decode(flag),encoding='utf-8')#用base64解码再将其给txt变量
txt1 = txt1.split(" ",1)#切片并获取后半部分
txt1= base64.b64decode(txt1[1])#base64解码成纯数字形式
txt1=str(txt1,'utf-8')
ans=req.post(url=url, data={'margin':txt1})
print(ans.text)
