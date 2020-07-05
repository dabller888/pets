#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Spider.py
@Time    :   2020/06/30 19:39:19
@Author  :   iceld 
@Version :   1.0
@Contact :   dabller888@163.com
@License :   (C)Copyright 2020-2022
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re
import threading
import time
import threading

def getPageData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find_all('div', class_='newslist')[0]
        a = re.findall('<dt><a.*?>(.*?)</a>', str(div))
        for i in a:
            print(i.strip())
    except Exception as ex:
        print(u'读取网页错误'+str(ex))


# 1.直接执行
# if __name__ == "__main__":
#     url = 'http://www.qiaoya.com/business_list.aspx?category_id=6&page='
#     stime = time.time()
#     for i in range(1, 5):
#         getPageData(url+str(i))

#     etime = time.time()
#     print('执行消耗时间：{0}s'.format(etime-stime))

# 2.多线程执行
if __name__ == "__main__":
    url = 'http://www.qiaoya.com/business_list.aspx?category_id=6&page='
    stime = time.time()
    for i in range(1, 5):
        url = url+str(i)
        t = threading.Thread(target=getPageData, args=(url,))
        t.start()

    etime = time.time()
    print('执行消耗时间：{0}s'.format(etime-stime))
