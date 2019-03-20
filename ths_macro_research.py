#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
from datetime import datetime, date, time
import requests
from lxml import etree


def get_list(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    MyPage = requests.get(url, headers=headers).content.decode("UTF-8")
    dom = etree.HTML(MyPage)

    listnews = dom.xpath('//a[@class="viewzy"]/@href')

    for news in listnews:
        # print(news)
        Page_Info('http://vis.10jqka.com.cn{}'.format(news))


def Page_Info(news):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}

    MyPage = requests.get(news, headers=headers).content.decode('utf-8')

    dom = etree.HTML(MyPage)
    # # content long
    items = dom.xpath('//div[@class="text"]/text()')
    items = "".join(items)
    # print(items)
    # file = open('content.txt', 'a+')
    # file.write(str(items))
    # file.close()
    # print(items)
    if items:
        urls.append(news)
        contents.append(items)

   
if __name__ == '__main__':
    urls = []
    contents = []
    
    for i in range(1, 11121):
        url = 'http://vis.10jqka.com.cn/free/ybzx/index/ctime/1/doSearch/1/pageNum/11120/curPage/{}'.format(i)
        print(url)
        get_list(url)

    df = pd.DataFrame({'url': list(urls), 'content': contents}, columns=['url', 'content'])
    df.to_csv('./ths_macro_research.csv')

    # time.sleep(random.randint(0, 3))  # 暂停0~3秒的整数秒，时间区间：[0,3]
