#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import httplib
import urllib
import urllib2
import time
import base64
import ssl
from sys import argv
def https_post_file(filename):
      ret=True
      try:
         context = ssl._create_unverified_context()
         data = []
         boundary = '----------%s' % hex(int(time.time() * 1000))
         data.append('--%s' % boundary)

         url = "https://%s:%s/upload_file.php" % ('10.95.41.15', '443')

         data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
         data.append(base64.b64encode(filename))
         data.append('--%s' % boundary)


         fr=open(filename,'rb')
         data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
         data.append('Content-Type: %s\r\n' % 'application/octet-stream')
         data.append(fr.read())
         fr.close()
         data.append('--%s--\r\n' % boundary)

         http_body='\r\n'.join(data)
         #   print http_body
         #buld http request
         req=urllib2.Request(url, data=http_body)
         #header
         req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
         req.add_header('User-Agent','Mozilla/5.0')
         req.add_header('Referer','http://10.95.41.15/')
         #post data to server
         resp = urllib2.urlopen(req, timeout=5,context = context)
         #get response
         qrcont=resp.read()
         #print qrcont
   
         return ret
      except Exception as e:
         #print(": unable to send URL: {0}".format(e))
    
         return False
      return
if __name__ == '__main__':
    
    filename = "../download/file"
    script= argv
    ret=https_post_file(filename)

    if ret:
        print("https upload file成功")
    else:
        print("https upload file失败")
