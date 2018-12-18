#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
import socket
import ssl
import paramiko
from socket import *
from sys import argv
def SSH2Test():
        ip = "10.95.41.15"
        cmd = ['pwd','echo hello!']#你要执行的命令列表
        username = "root"  #用户名
        passwd = "www.360.cn"    #密码
        ret = True
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip,22,username,passwd,timeout=120)
            ssh.exec_command("pwd")
            ssh.close()
            #print 'SSH connect %s\tOK\n'%(ip)
            return ret
        except :
            #print '%s\tError\n'%(ip)
            return False
        return

if __name__ == '__main__':

    script= argv
    ret=SSH2Test()

    if ret:
        print("SSH成功")
    else:
        print("SSH失败")
