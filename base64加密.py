
import base64
for i in range(10):
    bs=str(input("输入待转字符吧：")).encode()
    b64=str(base64.b64encode(bs),"utf-8")
    print("base64加密之后为:"+b64+"\n\n")
    # a85=str(base64.a85encode(bs),"utf-8")
    # print("a85加密为：\n\n",a85)

