#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
from sys import argv
def http_get():
   		ret=True
   		try:
	   		url = "http://www.baidu.com/s?wd=王宝强"
			req = urllib2.Request(url)
			#print req
			res_data = urllib2.urlopen(req)
			res = res_data.read()
			#print res

			return ret
		except Exception,e:
			print e

         	return False
		return
if __name__ == '__main__':

    script= argv
    ret=http_get()

    if ret:
        print("http_get成功")
    else:
        print("http_get失败")
