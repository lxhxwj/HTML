#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import json
import paramiko
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

def sftp_up():
    #if _DEBUG == True:
        #import pdb
        #pdb.set_trace()
    ret=True


   
    host = '10.95.41.15'
    port = 22
    username = 'root'
    password = 'www.360.cn'
    
    local = '../download/file'
    remote = '/home/test/file.sftp'
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local, remote)
        t.close()
   
        return True
    except Exception, e:
        print e
    
        return False


if __name__ == '__main__':
    file = "../download/file"
    script= argv
    ret = sftp_up()
    if ret:
	print "SFTP UPLOAD OK"
    else:
        print "SFTP UPLOAD FAIL"
