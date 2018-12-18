#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
import ssl
from sys import argv
def https_content():
      ret=True
      try:      
         #定义一个要提交的数据数组(字典) 
	 context = ssl._create_unverified_context()
         url = 'https://10.95.41.15/php/post.php'
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
         request = urllib2.Request(url, headers = headers)
         data = {}
         data['contents'] = 'wangbaoqiang王宝强'
         #data['fileImage'] = '123456' 
         #定义post的地址
         post_data = urllib.urlencode(data)
         #提交，发送数据
         req = urllib2.urlopen(url, post_data,context = context)
         #获取提交后返回的信息
         content = req.read()
         #return content
        
         return ret   
      except Exception,e:
         print e
       
         return False
if __name__ == '__main__':

    script= argv
    ret=https_content()

    if ret:
        print("https post content成功")
    else:
        print("https post content失败")
