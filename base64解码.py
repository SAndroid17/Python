
import base64
bs=str(input("输入待转字符吧（例如：cHl0aG9u）：")).encode()
print("待转字符为:",bs)
try:
    b64=str(base64.b64decode(bs),"utf-8")#64解码
    print("转换后的base64：", b64).encode("utf-8")#转后的base64代码
except :
    print('不是base64编码')
# --------------------------------------
try:
    bs32=str(base64.b32decode(bs),'utf-8')#32解码
    print("转换后的base32：", bs32)
except Exception as e:
    print('不是base32编码')
# --------------------------------------
try:
    a85=str(base64.a85decode(bs),'utf-8')#a85解码
    print("转换后的basebasea85：", a85)
except Exception as e:
    print('不是basea85编码')
# --------------------------------------
try:
    b85=str(base64.b85decode(bs),'utf-8')#b85解码
    print("转换后的baseb85：", b85)
except Exception as e:
    print('不是b85编码')
# --------------------------------------
try:
    b16=str(base64.b16decode(bs),'utf-8')#b16解码
    print("转换后的baseb16：", b16)
except Exception as e:
    print('不是b16编码')
# --------------------------------------
try:
    sbs64=str(base64.standard_b64decode(bs),'utf-8')#标准64解码
    print("转换后的标准base64标准：", sbs64)
except Exception as e:
    print('不是标准base64编码')