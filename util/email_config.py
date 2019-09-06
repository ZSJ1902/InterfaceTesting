#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   email_config.py
@Time    :   2019/9/5 18:58
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   发送邮件配置
"""

import smtplib
from email.mime.text import MIMEText

class EmailConfig(object):

    global send_user
    global mail_host
    global password
    send_user = '********@163.com'
    mail_host = 'smtp.163.com'
    password = '**********'

    def send_config(self, user_lists, subject, content):
        user = "发件人昵称" + "<" + send_user + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ";".join(user_lists)

        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(send_user, password)
        server.sendmail(user, user_lists, message.as_string())
        server.close()

    def send_mail(self, pass_cases, fail_cases):
        pass_num = float(len(pass_cases))
        fail_num = float(len(fail_cases))
        count_num = float(pass_num + fail_num)
        pass_ratio = "%.2f%%" % (pass_num / count_num * 100)
        fail_ratio = "%.2f%%" % (fail_num / count_num * 100)

        user_lists = ['********@foxmail.com']
        subject = "【邮件配置测试】"
        content = "一共执行 %f 个用例, 成功 %f 个，通过率为 %s；失败 %f 个，失败率为 %s。" % (count_num, pass_num, pass_ratio, fail_num, fail_ratio)

        self.send_config(user_lists, subject, content)


if __name__ == "__main__":
    ec = EmailConfig()
    ec.send_mail([1, 3, 5], [2, 4, 6])
