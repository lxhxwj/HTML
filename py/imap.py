#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
#import getpass, email, sys
#from imapclient import IMAPClient

import imaplib
import email
import string

import imaplib
 
connection = imaplib.IMAP4_SSL('imap.126.com', 993)
#connection = imaplib.IMAP4('imap.126.com')
# 使用imap，比如要访问163邮箱，地址是imap.163.com，而不是mail.163.com
 
username = 'datasec360'
password = 'Aa123456'
 
# 登陆
try:
    connection.login(username, password)
except Exception as err:
    print('登陆失败: :', err)  # 输出登陆失败的原因

res,data = connection.list()
print('Response code:', res)
print(data) 




res, data = connection.select('INBOX')
print(res, data)
print(data[0])  # 邮件数
# OK [b'110']
# b'110'



# 输出日志
#connection.print_log()
 
# 断开连接
#connection.close()
connection.logout()
