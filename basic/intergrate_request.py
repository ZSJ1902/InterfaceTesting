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


class IntergrateRequest(object):
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

    def main_req(self, method, url, data, headers):
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
    # get_method = 'get'
    # get_url = 'http://127.0.0.1:8000/query_article/'
    # get_data = None
    # get_header = None
    # print(ir.main_req(get_method, get_url, get_data, get_header))

    post_method = 'post'
    post_url = 'http://127.0.0.1:8000/add_article/'
    post_data = {
        "title": "intergrate_title",
        "content": "intergrate request"
    }
    post_headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "0a6db4e59c7fff2b2b94a297e2e5632e"
    }
    print(ir.main_req(post_method, post_url, post_data, post_headers))
