#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   interface_crud_tests.py
@Time    :   2019/9/4 14:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import requests
import unittest

class TestInterfaceCrud(unittest.TestCase):
    @unittest.skip("跳过测试")
    def test_query_article(self):
        payload = {}
        res = requests.get('http://127.0.0.1:8000/query_article/', params=payload)
        print("test_query_article: ", res.text)

    @unittest.skip("跳过测试")
    def test_add_article(self):
        payload = {
            "title": "title8",
            "content": "content8",
        }
        res = requests.post('http://127.0.0.1:8000/add_article/', json=payload)
        print(res.request)
        print(res.text)

    @unittest.skip("跳过测试")
    def test_modify_article(self):
        payload = {
            "title": "title1",
            "content": "content1",
        }
        res = requests.post('http://127.0.0.1:8000/modify_article/1', json=payload)
        print(res.request)
        print(res.text)

    # @unittest.skip("跳过测试")
    def test_delete_article(self):
        payload = {
            "title": "title2",
            "content": "content2",
        }
        res = requests.delete('http://127.0.0.1:8000/delete_article/2', json=payload)
        print(res.request)
        print(res.text)

    @unittest.skip("跳过测试")
    def test_test_api(self):
        payload = {
            'title': 'title1',
            'content': 'content1',
            'status': 'alive'
        }
        res = requests.post('http://127.0.0.1:8000/test_api/')
        print(res.text)


if __name__ == '__main__':
    unittest.main()
