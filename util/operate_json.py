#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   operate_json.py
@Time    :   2019/9/5 12:24
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   操作 JSON 文件中的数据
"""
import json
import os

curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.abspath(os.path.dirname(curPath))
print(rootPath)


class OperateJson(object):
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            # self.file_name = '../data/util_data/operate_json.json'
            self.file_name = r"data/TestcaseHeaders.json"
            self.file_name = os.path.join(rootPath, self.file_name)
            print("self.file_name: ", self.file_name)

        self.data = self.get_json()

    # 读取 json 文件
    def get_json(self):
        with open(self.file_name, encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    # 根据关键词读取数据
    def get_key_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    oj = OperateJson("../data/TestcaseHeaders.json")
    print(oj.get_json())
    # print('login: ', oj.get_key_data("login"))
    # print('login.username: ', oj.get_key_data("login")["username"])
    # print('login.password: ', oj.get_key_data("login")["username"])
    # print('logout: ', oj.get_key_data("logout"))
    # print('logout.code: ', oj.get_key_data("logout")["code"])
    # print('logout.info: ', oj.get_key_data("logout")["info"])
