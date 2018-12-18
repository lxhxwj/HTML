#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import smtplib
import os
import time
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
	time.sleep(3)
	os.system('mail -s "王宝强" datasec360@126.com < /var/www/html/upload/att.txt')	
    except Exception:
        ret=False
    return ret

if __name__ == '__main__':

    script= argv
    
   
    while True:
	time.sleep(10*6)
	mail()
	
#    ret=mail()

#    if ret:
#        print("邮件发送成功")
#    else:
#        print("邮件发送失败")
