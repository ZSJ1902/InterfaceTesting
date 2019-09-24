#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   baidu_translate.py
@Time    :   2019/9/2 20:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import requests
import random
import hashlib
import urllib
import json


class BaiduTranslate(object):
    def __init__(self, word):
        # 你要翻译的元素
        self.q = word
        self.fromLang = 'en'
        self.toLang = 'zh'
        self.baidu_translate = 'https://api.fanyi.baidu.com/'
        self.translate_api_url = '/api/trans/vip/translate'

        # 百度开发者配置信息
        self.appid = '20190508000295298'
        self.secretKey = 'SpZnEM6HliTHK1Mlp96I'

        # 开发配置
        self.salt = random.randint(32768, 65536)
        self.sign = self.appid + self.q + str(self.salt) + self.secretKey
        m1 = hashlib.md5()
        m1.update(self.sign.encode('utf-8'))
        self.sign = m1.hexdigest()
        self.my_url = self.translate_api_url + '?appid=' + self.appid + '&q=' + urllib.request.quote(self.q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(self.salt) + '&sign=' + self.sign

    def en_translate_zh(self):
        re = requests.request("post", self.baidu_translate + self.my_url)
        print('\n\t re.text', re.text)
        re_json = json.loads(re.text)
        print('\n\t re_json', re_json)


if __name__ == "__main__":
    bt = BaiduTranslate('test')
    bt.en_translate_zh()
