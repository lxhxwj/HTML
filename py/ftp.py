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
    #��ʾftp��������ӭ��Ϣ
    ftp.cwd('test')
    #ѡ�����Ŀ¼
    bufsize = 1024
    filename = "/var/www/html/guanjianzi.txt"
    file_handler = open(filename,'wb').write
    #��дģʽ�ڱ��ش��ļ�
    ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handler,bufsize)
    #���շ��������ļ���д�뱾���ļ�
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
        #�򿪵��Լ���2����ʾ��ϸ��Ϣ;0Ϊ�رյ�����Ϣ
        ftp.connect('10.95.41.15','21')
        #����
        ftp.login('test','1')
        #��¼�����������¼���ÿմ����漴��
        #print ftp.getwelcome()
        #��ʾftp��������ӭ��Ϣ
        ftp.cwd('FTP')
        #ѡ�����Ŀ¼
        bufsize = 1024
        #���û�����С
        file_handler = open(filename,'rb')
        #�Զ�ģʽ�ڱ��ش��ļ�
        ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)
        #�ϴ��ļ�
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
