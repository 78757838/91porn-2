#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/03/2018 12:56 AM
# @Author  : Fish
# @Site    : 
# @File    : testproxy.py
# @Software: PyCharm

import socket
import socks
import requests
import configparser

def set_proxy():
    config = configparser.ConfigParser()
    config.read('config.txt')

    enable = config.get('proxy', 'enable')
    http_proxy = config.get('proxy', 'http_proxy')
    socks5 = config.get('proxy', 'socks5')
    if enable =='1' and len(http_proxy) >0:
        pass
    elif enable =='1' and len(socks5) > 0:
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9137)
        socket.socket = socks.socksocket
        # print(requests.get('http://ip.cn').text)
