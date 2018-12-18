#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
from sys import argv
def http_content():
      ret=True
      try:      
         #定义一个要提交的数据数组(字典)
         data = {}
         data['contents'] = 'wangbaoqiang王宝强'
         #data['fileImage'] = '123456' 
         #定义post的地址
         url = 'http://10.95.41.15:8000/php/post.php'
         post_data = urllib.urlencode(data) 
         #提交，发送数据
         req = urllib2.urlopen(url, post_data) 
         #获取提交后返回的信息
         content = req.read()
         #return content
   
         return ret   
      except Exception,e:
         print e
    
         return False
      return
		
if __name__ == '__main__':

    script= argv
    ret=http_content()

    if ret:
        print("http post content成功")
    else:
        print("http post content失败")
