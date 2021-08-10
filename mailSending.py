#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendmail(content):
    # 获取邮箱相关信息
    try:
        with open('./Account.txt', 'r') as f:
            # 第三方 SMTP 服务
            lines = f.readlines()
            mail_host = lines[2].replace("\n", "").replace("\r", "").replace(" ", "")  # 设置服务器
            mail_user = lines[3].replace("\n", "").replace("\r", "").replace(" ", "")  # 用户名
            mail_pass = lines[4].replace("\n", "").replace("\r", "").replace(" ", "")  # 口令
            mail_recv = lines[5].replace("\n", "").replace("\r", "").replace(" ", "")  # 口令
            print("发送邮件使用的邮箱为:", mail_user)
    except FileNotFoundError as e:
        print("没有找到Account.txt文件，请查看该文件！")
        exit(0)

    sender = mail_user
    receivers = list()  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers.append(mail_recv)

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


if __name__ == "__main__":
    sendmail('测试')
