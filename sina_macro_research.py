#!/usr/bin/env python
# -*- coding: utf-8  -*-

import json
import pandas as pd
import requests
import re
import sys
from datetime import datetime
import requests
from lxml import etree

def get_list(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    MyPage = requests.get(url, headers=headers).content.decode("gbk")
    dom = etree.HTML(MyPage)
    listnews = dom.xpath('//td[@class="tal f14"]/a[@target="_blank"]/@href')

    # print(listnews)
    # print(len(listnews))
    for child_url in listnews:
        # print(news)
        Page_Info(child_url)

def Page_Info(child_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}

    MyPage = requests.get(child_url, headers=headers).content.decode('gbk')

    dom = etree.HTML(MyPage)
    # # content long
    items = dom.xpath('//div[@class="blk_container"]/p/text()')
    url_date = dom.xpath('//div[@class="creab"]/span/text()')
    url_date = datetime.strptime(url_date[-1][3:], "%Y-%m-%d").strftime('%Y%m%d')
    # print(items)
    # print(url_date)
    # print(child_url)

    if items:
        times.append(url_date)
        urls.append(child_url)
        contents.append(items)


if __name__ == '__main__':
    urls = []
    times = []
    contents = []

    for i in range(1, 1884):
        url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/macro/index.phtml?p={}'.format(i)
        print(url)
        get_list(url)

    # get_list('http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/macro/index.phtml?p=1558')
    df = pd.DataFrame({'url': list(urls), 'time': times, 'content': contents}, columns=['time', 'url', 'content'])
    df.to_csv('./sina_macro_research.csv')
  
