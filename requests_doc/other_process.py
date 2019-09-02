#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   other_process.py
@Time    :   2019/9/2 17:46
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import requests
import time

url = 'https://httpbin.org/get'

def operator_cookies():
    r = requests.get(url)
    print('r.cookies: ', r.cookies)

    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    r2 = requests.get(url=url, cookies=jar)
    print('r2.text', r2.text)


operator_cookies()


def request_history():
    r = requests.get(url=url)
    print('r.history: ', r.history)


request_history()


def timeout():
    print(time.time())
    print(time.time())
    r = requests.get(url, timeout=5)
    print(time.time())


# timeout()
