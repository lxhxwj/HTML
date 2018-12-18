#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import json
#_DEBUG=True
from ftplib import FTP
from sys import argv


def ftp_down(filename = "/var/www/html/guanjianzi.txt"):
    ftp=FTP()
    ftp.set_debuglevel(0)
    ftp.connect('10.95.41.18','21')
    ftp.login('test','1')
    #print ftp.getwelcome()
    #显示ftp服务器欢迎信息
    ftp.cwd('test')
    #选择操作目录
    bufsize = 1024
    filename = "/var/www/html/guanjianzi.txt"
    file_handler = open(filename,'wb').write
    #以写模式在本地打开文件
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)
    #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)
    file_handler.close()
    ftp.quit()

def upload(filename):
    #if _DEBUG == True:
        #import pdb
        #pdb.set_trace()
    ret=True
    try:
        ftp=FTP()
        #ftp.set_debuglevel(0)
        #打开调试级别2，显示详细信息;0为关闭调试信息
        ftp.connect('10.95.41.15','21')
        #连接
        ftp.login('test','1')
        #登录，如果匿名登录则用空串代替即可
        #print ftp.getwelcome()
        #显示ftp服务器欢迎信息
        ftp.cwd('FTP')
        #选择操作目录
        bufsize = 1024
        #设置缓冲块大小
        file_handler = open(filename,'rb')
        #以读模式在本地打开文件
        ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
        #上传文件
        #ftp.set_debuglevel(0)
        file_handler.close()
        ftp.quit()

    except Exception:
        ret=False
    return ret


if __name__ == '__main__':
    file = "../download/file"
    script= argv
    ret = upload(file)
    if ret:
        print "FTP UPLOAD OK"
    else:
        print "FTP UPLOAD FAIL"
