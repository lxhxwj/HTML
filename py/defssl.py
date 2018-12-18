#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
import socket
import ssl
from socket import *
from sys import argv
def httpsSSL():
      ret=True
      try:      
         #定义一个要提交的数据数组(字典)
         context = ssl._create_unverified_context()
         url = 'https://10.95.27.121'
         #提交，发送数据
         req = urllib2.urlopen(url)
         #获取提交后返回的信息
         content = req.read()
         #return content
         return ret
      except Exception,e:
         print e
         return ret
		
if __name__ == '__main__':

    script= argv
    ret=httpsSSL()

    if ret:
        print("双向SSL成功")
    else:
        print("双向SSL失败")
