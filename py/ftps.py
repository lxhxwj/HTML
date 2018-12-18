#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import json
import ftplib
import socket
import ssl
#_DEBUG=True
from sys import argv

class FTP_TLS(ftplib.FTP_TLS):
    def __init__(self, host='', user='', passwd='', acct='', keyfile=None, certfile=None, context=None, timeout=180):
        ftplib.FTP_TLS.__init__(self, host, user, passwd, acct, keyfile, certfile, context, timeout)
    def connect(self, host='', port=0, timeout=-999):
        if host != '':
            self.host = host
        if port > 0:
            self.port = port
        if timeout != -999:
            self.timeout = timeout

        try:
            self.sock = socket.create_connection((self.host, self.port), self.timeout)
            self.af = self.sock.family
            self.sock = ssl.wrap_socket(self.sock, self.keyfile, self.certfile, ssl_version=ssl.PROTOCOL_TLSv1)
            self.file = self.sock.makefile('rb')
            self.welcome = self.getresp()
        except Exception as e:
            print e
        return self.welcome
    def download(self, remote_file_name, local_file_name):
        with open(local_file_name, 'wb') as fp:
            self.retrbinary('RETR %s' % remote_file_name, fp.write)
    def upload(self, local_file_name):
	file_handler = open(local_file_name,'rb')
	bufsize = 1024
	#self.retrbinary('RETR %s' % remote_file_name, fp.write)
	self.storbinary('STOR %s' % os.path.basename(local_file_name),file_handler,bufsize)

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

def upload():
    host = '10.95.41.18'
    port = 990
    user = 'test'
    password = '1'
    #if _DEBUG == True:
        #import pdb
        #pdb.set_trace()
    ret=True
    try:
	ftps = FTP_TLS()	
    	ftps.connect(host, port)
   	ftps.login(user, password)   
    	ftps.prot_p()
	ftps.set_pasv(True)
	local_file_name ='../download/file'
	ftps.cwd("test")

	file_handler = open(local_file_name,'rb')
        bufsize = 1024
 	
        ftps.storbinary('STOR %s' % os.path.basename(local_file_name),file_handler,bufsize)
   
  
    except Exception:
	ret=False
    return ret


if __name__ == '__main__':
   
    script= argv
    ret = upload()
    if ret:
        print "FTPS UPLOAD OK"
    else:
        print "FTPS UPLOAD FAIL"
