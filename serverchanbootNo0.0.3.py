# coding= utf-8
import requests,urllib.request,socket,re,time
url = "yourURL"
title = "设备已经启动"
#常量定义
time.sleep(10)
getip=urllib.request.urlopen('http://ip.42.pl/raw')
getip2=getip.read()
string_ip = str(getip2)
#获取ip地址
ip = str(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",string_ip))
#格式化ip地址
pcname = socket.gethostname()
dataout = str("主机名:"+pcname+"设备公网ip地址:"+ip)
data={"text":title,"desp":dataout}
requests.post(url,data=data)
#请求ServerchanAPI