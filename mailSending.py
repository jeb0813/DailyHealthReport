#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendmail(content: str):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1258975239@qq.com"  # 用户名
    mail_pass = "lvqqutdgexxgjhji"  # 口令

    sender = '1258975239@qq.com'
    receivers = ['978364075@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # content = '填写成功'
    subject = '健康日报填写自动化'
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("健康日报机器人", 'utf-8')
    message['To'] = Header("978364075@qq.com", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8').encode()

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.set_debuglevel(0)
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
