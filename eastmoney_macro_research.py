#!/usr/bin/env python
# -*- coding: utf-8  -*-

import json
import pandas as pd
import requests
import re
import sys
from datetime import datetime, date, time
import requests
from lxml import etree
import pandas as pd


def get_list(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    # str
    MyPage = requests.get(url, headers=headers).content.decode("UTF-8")
    MyPage = MyPage[2:-2].split('","')
    MyPage = [_.strip('"') for _ in MyPage]
    for _ in MyPage:
        _ = _.split(',')

        # string转datetime : datetime.strptime
        # datetime转string : strftime
        url_date = datetime.strptime(_[0], "%Y/%m/%d %H:%M:%S").strftime('%Y%m%d')
        num = _[1]
        child_url = 'http://data.eastmoney.com/report/{}/hg,{}.html'.format(url_date, num)
        print(child_url)
        # times.append(url_date)
        # urls.append(child_url)
        Page_Info(url_date, child_url)


def Page_Info(url_date, child_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}

    MyPage = requests.get(child_url, headers=headers).content.decode("gbk")

    dom = etree.HTML(MyPage)
    # # content long
    # items = dom.xpath('//div[@class="newsContent"]/text()')
    items = dom.xpath('//div[@class="newsContent"]/p/text()')
    items = "".join(items)
    print(child_url)



if __name__ == '__main__':
    urls = []
    times = []
    contents = []

    for i in range(1, 239):
        url = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HGYJ&cmd=4&code=&ps=50&p={}'.format(i)
        print(url)
        get_list(url)

    # # test for one
    # url = 'http://datainterface.eastmoney.com//EM_DataCenter/js.aspx?type=SR&sty=HGYJ&cmd=4&code=&ps=50&p=3'
    # get_list(url)

    df = pd.DataFrame({'url': list(urls), 'time': times, 'content': contents}, columns=['time', 'url', 'content'])
    df.to_csv('./eastmoney_macro_research.csv')

    # time.sleep(random.randint(0, 3))  # 暂停0~3秒的整数秒，时间区间：[0,3]

