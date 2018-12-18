#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import telnetlib
import httplib
import urllib
import urllib2
import socket
import time
from socket import *
from sys import argv

def TelnetTestFile():
	tn = telnetlib.Telnet()
	tn.open('10.95.27.76', 2425)
	f = open('../download/file',"r")
	time.sleep(1)
	f_body = f.read()
	time.sleep(1)
	tn.write(f_body)
	tn.write("n")
	f.close()
	tn.close()

	return True	
if __name__ == '__main__':

    script= argv
    ret=TelnetTestFile()

    if ret:
        print("socket 成功")
    else:
        print("socket 失败")
