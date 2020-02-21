from urllib.parse import unquote
from urllib.parse import quote
text=input("请输入解码的字符串：")
try:
    text1 = unquote(text, 'utf-8')#解码
    text2 = quote(text, 'utf-8')#编码
    print("URL编码前：",text1+"\n","\nURL编码后：",text2)
except Exception as e:
    print('不能解码')
