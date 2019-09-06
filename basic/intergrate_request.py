#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   intergrate_request.py
@Time    :   2019/9/6 7:56
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   多种请求方法集成
"""

import requests
import json


class IntergrateRequest():
    # 请求 request方法
    def get_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.get(url, data, headers).json()
        else:
            res = requests.get(url,  data).json()
        return res

    # post 请求方式
    def post_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.post(url, data, headers).json()
        else:
            res = requests.post(url,  data).json()
        return res

    # delete 请求方式
    def delete_req(self, url, data=None, headers=None):
        if headers is not None:
            res = requests.delete(url, data, headers).json()
        else:
            res = requests.delete(url,  data).json()
        return res

    def main_req(self, method, url, data=None, headers=None):
        if method == "get":
            res = self.get_req(url, data, headers)
        elif method == 'post':
            res = self.post_req(url, data, headers)
        elif method == 'delete':
            res = self.delete_req(url, data, headers)
        else:
            res = "你的请求方式暂未开放，请耐心等待"
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    ir = IntergrateRequest()
    method = 'get'
    url = 'http://127.0.0.1:8000/query_article/'
    data = None
    headers = None
    print(ir.main_req(method, url, data, headers))


