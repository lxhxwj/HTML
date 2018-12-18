#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
import socket
from socket import *
from sys import argv

def SendMessageForFeiqTCP():
	ip = '10.95.27.76'
	#s=socket(AF_INET,SOCK_STREAM)
	s=socket(AF_INET,SOCK_DGRAM)
        s.connect((ip, 2425))
        a = u"1:525:杨曙光:杨曙光:32:我是王宝强，我无敌!"
        s.send(a.encode("gbk"))
        s.close()
        #print u'(未知协议) socket OK'
        return True     
		
if __name__ == '__main__':

    script= argv
    ret=SendMessageForFeiqTCP()

    if ret:
        print("socket 成功")
    else:
        print("socket 失败")
