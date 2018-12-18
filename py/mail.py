#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import smtplib
import os
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
	os.system('echo "涉密邮件:王宝强" | /bin/mail -s "王宝强" datasec360@126.com')
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
