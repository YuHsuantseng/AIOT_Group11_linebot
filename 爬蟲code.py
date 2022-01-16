# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 13:17:57 2021

@author: user
"""

import requests
from bs4 import BeautifulSoup
import re
#給一個假定的使用者，讓google不要被偵測到是在刷機
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
headers = {"user-agent" : MOBILE_USER_AGENT}
keyword_ar = ["買", "看", "聽", ]
#"我要買iphone13", "什麼是電腦", "我想看月老", "我想聽梁靜茹的勇氣"
request = "我想聽梁靜茹的勇氣"
for key_index in range(0, len(keyword_ar)): #檢查請求有沒有keyword_ar的關鍵字 
    if keyword_ar[key_index] in request:
        keyword = request[request.rfind(keyword_ar[key_index]) :]
        break
    if key_index == len(keyword_ar)-1:
        keyword = request
URL = 'https://www.google.com/search?q={}'.format(keyword)

resp = requests.get(URL, headers=headers)
soup = BeautifulSoup(resp.content, "html.parser")
a_tags = soup.find_all('a')
for tag in a_tags:
    response = tag.get('href')
    if response and 'https://' in response and 'google' not in response:
        result = response
        break
print(result)


