# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:28:44 2022

@author: fapeng
"""

# -*- coding: utf-8 -*-
#!/usr/bin/python3

import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
from urllib.request import urlopen
from json import load
timestamp = str(round(time.time() * 1000))
#输入加签密钥
secret = 'XXX'
#上面输入
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
def get_ip_a():
    my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']# 获取ipv4地址
    print('api.ipify.org', my_ip)
    
    ip = urlopen('https://api-ipv6.ip.sb/ip').read()  # 使用IP.SB的接口获取ipv6地址
    ipv6 = str(ip, encoding='utf-8')
    print("获取到IPv6地址：%s" % ipv6)
    #print("Date >> 当前公网IP ", my_ip, "\n")
    return ip
    
def message():
    ipv6=get_ip_a().decode('utf-8')
    test=""
    message="ipv6 "+test+ipv6
    return message

def run():
    #更改webhook
    Webhook="XXX"
    #此处修改
    post_url = Webhook+"&timestamp="+timestamp+"&sign="+sign+""
    msg= message()
    headers = {'Content-Type': 'application/json'}
    data =  {
    "msgtype": "text",
     "text": {
         "content":msg
    }
    }
    requests.post(post_url, data=json.dumps(data), headers=headers)

run()