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
	os.system('export LANG=utf-8')
	os.system("ps -ef | grep loopmail | awk '{print $2}' | xargs kill -9")
    except Exception:
        ret=False
    return ret

if __name__ == '__main__':

    script= argv
    ret=mail()

    if ret:
        print("进程成功杀死")
    else:
        print("失败")
