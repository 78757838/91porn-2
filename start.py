#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/03/2018 11:12 PM
# @Author  : Fish
# @Site    : 
# @File    : start.py
# @Software: PyCharm

from component import porn,downloader,utility

page_num = utility.get_page_num()
url=utility.get_url()

for n in range(int(page_num) + 1):
    page_url = url + '?category=rf&page=' + str(n)

mm = porn.Porn(page_url)
content = mm.get_home_page_txt()
video_dict = mm.get_video_link(content)

for video_name,url in video_dict.items():
    print("视频名: %s url: %s" %(video_name,url))
    download = downloader.Downloader(video_name, url)
    download.run()
