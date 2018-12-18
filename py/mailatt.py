#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import smtplib
import os
import subprocess
from email.mime.text import MIMEText
from email.utils import formataddr
from sys import argv


def mail():
    #if _DEBUG == True:
        #import pdb
        #pdb.set_trace()

#    print my_sender
#    print my_user


    ret=True
    try:
	os.system('mail -s "王宝强" datasec360@126.com < /var/www/html/upload/att.txt') 
	#print subprocess.call('/usr/bin/mutt datasec360@126.com -s "王宝强的邮件" -a /var/www/html/upload/att.txt </var/www/html/upload/con.txt',shell=True)
    except Exception:
        ret=False
    return ret

if __name__ == '__main__':

    script= argv
    ret=mail()

    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
