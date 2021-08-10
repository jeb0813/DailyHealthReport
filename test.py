import ssl
import requests
from urllib.parse import urlencode
# from bs4 import BeautifulSoup
import requests
# import bs4
import re
# import re
# 配置文件
import configparser
# from datetime import *

# import pymysql
import os
import cx_Oracle
import urllib.parse
import datetime
# from datetime import datetime
import time
import pythoncom

import xlrd, xlwt
from xlutils.copy import copy
from shutil import copyfile
import os

import math

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

# import excel_to_pic
from PIL import ImageGrab
import xlwings as xw

# mail 相关库
import traceback
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import random


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'gbk').encode(), addr))
    # return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(to_addr_in, file_in, mail_subject, mail_content, mail_user, mail_pwd, att_file):
    # 邮件发送和接收人配置
    # from_addr = 'chenjianhai.sq'
    from_addr = mail_user
    smtp_server = mail_smtp
    # password = 'Sqdxcjh_8813'  #这是你邮箱的第三方授权客户端密码，并非你的登录密码
    password = mail_pwd
    to_addr = to_addr_in
    to_addrs = to_addr.split(',')

    msg = MIMEMultipart()
    # msg['From'] = _format_addr('自动发送邮件 <%s>' % from_addr)  # 显示的发件人
    msg['From'] = _format_addr(from_addr)  # 显示的发件人
    # msg['To'] = _format_addr('管理员 <%s>' % to_addr)                # 单个显示的收件人
    msg['To'] = ",".join(to_addrs)  # 多个显示的收件人
    msg['Subject'] = Header(mail_subject, 'utf-8').encode()  # 显示的邮件标题

    # 邮件正文是MIMEText:
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    basename = os.path.basename(file_in)
    # file_in1 = basename.encode('gbk')
    file_in1 = basename  # .encode('gbk')

    print(file_in, file_in1)
    mime = MIMEBase('file', 'xls', filename=file_in1)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=file_in1)  # .encode('gb2312'))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    # mime.set_payload(file_in.read())
    f = open(file_in, 'rb')
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

    # 增加附件
    if att_file != '':
        print(att_file)
        basename = os.path.basename(att_file)
        # file_in1 = basename.encode('gbk')
        file_in2 = basename  # .encode('gbk')

        print(att_file, file_in2)
        mime1 = MIMEBase('file', 'xls', filename=file_in2)
        # 加上必要的头信息:
        mime1.add_header('Content-Disposition', 'attachment', filename=file_in2)  # .encode('gb2312'))
        mime1.add_header('Content-ID', '<0>')
        mime1.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        # mime.set_payload(file_in.read())
        f1 = open(att_file, 'rb')
        mime1.set_payload(f1.read())
        # 用Base64编码:
        encoders.encode_base64(mime1)
        # 添加到MIMEMultipart:
        msg.attach(mime1)

    try:
        server = smtplib.SMTP(smtp_server)
        # server.starttls()
        server.set_debuglevel(0)  # 用于显示邮件发送的执行步骤
        server.login(from_addr, password)

        # print to_addrs
        server.sendmail(from_addr, to_addrs, msg.as_string())
        # server.sendmail(from_addr, to_addrs, msg.as_string())
        # log='邮件地址：'+to_addr+'；文件名;'+file_name+'邮件发送成功'
        # print(log)
        # write_log(log)
        server.quit()

    except Exception:
        print("Error: unable to send email, 邮件发送错误，请检查网络、核验用户名称与密码是否准确。")
        log = "Error: unable to send email,邮件发送错误，请检查网络、核验用户名称与密码是否准确。"
        # write_log(log)
