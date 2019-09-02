#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   urllib_request.py
@Time    :   2019/9/2 20:49
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from urllib import request
from urllib import parse


def urllib_request():
    base_url = 'http://www.tuling123.com/openapi/api'
    payload = {
        'key1': 'Your',
        'key2': '你好'
    }

    ur = request.Request(url=base_url)
    ur_response = request.urlopen(ur)
    print('\n ur_response: \n\t', ur_response)
    print('\n ur_response_getcode: \n\t ', ur_response.getcode)
    print('\n ur_response_headers: \n\t ', ur_response.headers)

    data = parse.urlencode(payload).encode('utf-8')
    url_payload = request.Request(url=base_url, data=data)
    url_payload_response = request.urlopen(url_payload)

    print('\n url_payload_response: \n\t', url_payload_response)
    print('\n url_payload_response_getcode: \n\t ', url_payload_response.getcode)
    print('\n url_payload_response_headers: \n\t ', url_payload_response.headers)
    print('\n url_payload_response_msg: \n\t ', url_payload_response.msg)
    print('\n url_payload_response_read: \n\t ', url_payload_response.read)


urllib_request()
