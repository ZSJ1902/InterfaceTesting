#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   response_code.py
@Time    :   2019/9/2 15:41
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import requests


# 1. 返回接口状态码：200
def response_200_code():
    interface_200_url = 'https://httpbin.org/status/200'
    response_get = requests.get(interface_200_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_200_code()


# 2.返回接口状态码：400
def response_400_code():
    interface_400_url = 'https://httpbin.org/status/400'
    response_get = requests.get(interface_400_url)
    response_get_code = response_get.status_code
    print('response_get_code: ', response_get_code)


response_400_code()
