#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/03/2018 12:19 AM
# @Author  : Fish
# @Site    : 
# @File    : porn.py
# @Software: PyCharm

import http
import logging
import time
import requests
from component import proxy, utility



class Porn(object):
    def __init__(self,url):
        logging.debug("Porn init")
        proxy.set_proxy()
        self.url = url

    '''
    获取home页面内容txt
    '''
    def get_home_page_txt(self):
        print(self.url)
        try:
            reqs = requests.Session()
            return reqs.get(self.url, headers=utility.set_header()).text
        except ConnectionResetError:
            print('ConnectionResetError')
            time.sleep(10)
            return reqs.get(self.url, headers=utility.set_header()).text
        except http.client.IncompleteRead:
            print('http.client.IncompleteRead')
            time.sleep(10)
            return reqs.get(self.url, headers=utility.set_header()).text

    '''
    获取指定页面(视频页面)内容
    '''
    def get_page_txt(self,url):
        # print(url)
        req=requests.Session()
        content=req.get(url, headers=utility.set_header()).text
        return content

    '''
    获取视频链接字典
    {'G奶美空模特': 'http://185.38.13.159//mp43/259563.mp4?st=8LBTsHbwBgoMnQrMZP8DSQ&e=1522577665'}
    '''
    def get_video_link(self,page_content):
        video_link_pages= utility.filter_video_page(page_content)
        # print(video_link_pages)
        video_dict=dict()
        for link in video_link_pages:
            page = self.get_page_txt(link)
            # print(page)
            video_link= utility.filter_video_link(page)
            for title,url in video_link.items():
                video_dict[title]=url
        return video_dict

    def get_file(self,filename,url):
        session = requests.Session()
        req = session.get(url, headers=utility.set_header(), stream=True)
        with open(filename,'wb') as f:
            f.write(req.content)



