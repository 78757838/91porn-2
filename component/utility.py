#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/03/2018 12:40 AM
# @Author  : Fish
# @Site    : 
# @File    : utility.py
# @Software: PyCharm

import random
import configparser
import html5lib
from bs4 import BeautifulSoup as bs
import os
import configparser

'''
设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agent
'''
uas = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.96 Chrome/58.0.3029.96 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]


'''
伪造http头，突破每天10个限制
'''
def set_header():
    randomIP = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
        random.randint(0, 255)) + '.' + str(random.randint(0, 255))
    headers = {
        'User-Agent': random.choice(uas),
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        'X-Forwarded-For': randomIP,
    }
    return headers

'''
从配置文件读取url,然后加上 /index.php
'http://91porn.com' + '/index.php'
'''
def get_url():
    config = configparser.ConfigParser()
    config.read('config.txt')
    url=config.get('website','web_site')
    url.rstrip('/')
    url=url + '/index.php'
    return url

'''
查找 视频链接页面
<a target=blank href="http://91porn.com/view_video.php?viewkey=066ee6030e8a99bfd2cb"><span class="title">快插小主播｛2｝有完整版，｛广告合作｝</span></a>
'''
def filter_video_page(home_page_content):
    soup = bs(home_page_content, 'html5lib')
    videoPages = set()
    for link in soup.find_all('a'):
        # print(link.get('href'))
        ss = link.get('href')
        if len(ss) > 8 and ss.find('view_video') != -1:
            videoPages.add(ss)
    return videoPages

'''
根据视频页面: http://91porn.com/view_video.php?viewkey=066ee6030e8a99bfd2cb
提取视频链接: 
'''
def filter_video_link(video_page_content):
    result=dict()
    unicode_txt=video_page_content
    soup=bs(unicode_txt, 'html5lib')
    # video_url=soup.find('video').find('source').get('src').split('?')[0]
    video_url=soup.find('video').find('source').get('src')
    video_title=soup.find(id='viewvideo-title').get_text().strip()
    # return video_title,video_url
    result[video_title]=video_url
    return result

'''
创建下载文件夹
'''
def mk_download_dir():
    config = configparser.ConfigParser()
    config.read('config.txt')
    dir_name=config.get('download', 'dir_name')
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass
    return dir_name
'''
获取分页
'''
def get_page_num():
    config = configparser.ConfigParser()
    config.read('config.txt')
    page_num=config.get('download', 'page_num')
    return page_num