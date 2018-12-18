#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ftplib
import os
import sys
class FTPSync(object):
  conn = ftplib.FTP()
  def __init__(self,host,port=21):    
    self.conn.connect(host,port)    
  def login(self,username,password):
    self.conn.login(username,password)
    self.conn.set_pasv(False)
    print self.conn.welcome
  def test(self,ftp_path):
    print ftp_path
    print self._is_ftp_dir(ftp_path)
    #print self.conn.nlst(ftp_path)
    #self.conn.retrlines( 'LIST ./a/b')
    #ftp_parent_path = os.path.dirname(ftp_path)
    #ftp_dir_name = os.path.basename(ftp_path)
    #print ftp_parent_path
    #print ftp_dir_name
  def _is_ftp_file(self,ftp_path):
    try:
      if ftp_path in self.conn.nlst(os.path.dirname(ftp_path)):
        return True
      else:
        return False
    except ftplib.error_perm,e:
      return False
  def _ftp_list(self, line):
    list = line.split(' ')
    if self.ftp_dir_name==list[-1] and list[0].startswith('d'):
      self._is_dir = True
  def _is_ftp_dir(self,ftp_path):
    ftp_path = ftp_path.rstrip('/')
    ftp_parent_path = os.path.dirname(ftp_path)
    self.ftp_dir_name = os.path.basename(ftp_path)
    self._is_dir = False
    if ftp_path == '.' or ftp_path== './' or ftp_path=='':
      self._is_dir = True
    else:
      #this ues callback function ,that will change _is_dir value
      try:
        self.conn.retrlines('LIST %s' %ftp_parent_path,self._ftp_list)
      except ftplib.error_perm,e:
        return self._is_dir    
    return self._is_dir
  def get_file(self,ftp_path,local_path='.'):
    ftp_path = ftp_path.rstrip('/')
    if self._is_ftp_file(ftp_path):    
      file_name = os.path.basename(ftp_path)
      #�������·����Ŀ¼�������ļ�����Ŀ¼
      if os.path.isdir(local_path):
        file_handler = open(os.path.join(local_path,file_name), 'wb' )
        self.conn.retrbinary("RETR %s" %(ftp_path), file_handler.write) 
        file_handler.close()
      #�������·������Ŀ¼�����ϲ�Ŀ¼���ڣ����ձ���·�����ļ�����Ϊ���ص��ļ�����
      elif os.path.isdir(os.path.dirname(local_path)):
        file_handler = open(local_path, 'wb' )
        self.conn.retrbinary("RETR %s" %(ftp_path), file_handler.write) 
        file_handler.close()
      #�������·������Ŀ¼�����ϲ�Ŀ¼�����ڣ����˳�
      else:
        print 'EROOR:The dir:%s is not exist' %os.path.dirname(local_path)
    else:
      print 'EROOR:The ftp file:%s is not exist' %ftp_path
  def put_file(self,local_path,ftp_path='.'):
    ftp_path = ftp_path.rstrip('/')
    if os.path.isfile( local_path ):           
      file_handler = open(local_path, "r")
      local_file_name = os.path.basename(local_path)
      #���Զ��·���Ǹ�Ŀ¼�����ϴ��ļ������Ŀ¼���ļ�������
      if self._is_ftp_dir(ftp_path):
        self.conn.storbinary('STOR %s'%os.path.join(ftp_path,local_file_name), file_handler)
      #���Զ��·�����ϲ��Ǹ�Ŀ¼�����ϴ��ļ����ļ������ո�������
      elif self._is_ftp_dir(os.path.dirname(ftp_path)): 
        print 'STOR %s'%ftp_path        
        self.conn.storbinary('STOR %s'%ftp_path, file_handler)
      #���Զ��·������Ŀ¼������һ���Ŀ¼Ҳ�����ڣ�����ʾ����Զ��·������
      else:        
        print 'EROOR:The ftp path:%s is error' %ftp_path
      file_handler.close()
    else:
      print 'ERROR:The file:%s is not exist' %local_path
  def get_dir(self,ftp_path,local_path='.',begin=True): 
    ftp_path = ftp_path.rstrip('/')
    #��ftpĿ¼����ʱ����    
    if self._is_ftp_dir(ftp_path):
      #������ص����ص�ǰĿ¼�£�������Ŀ¼
      #���س�ʼ������������ı���·����������Ҫ������ͬʱ��ftp��Ŀ¼����ڸ����ı���Ŀ¼�¡�
      #ftpĿ¼���ļ���ŵ�·��Ϊlocal_path=local_path+os.path.basename(ftp_path)
      #���磺��ftp�ļ���a���ص����ص�a/bĿ¼�£���ftp��aĿ¼�µ��ļ������ص����ص�a/b/aĿ¼��
      if begin:
        if not os.path.isdir(local_path):
          os.makedirs(local_path)
        local_path=os.path.join(local_path,os.path.basename(ftp_path))
      #�������Ŀ¼�����ڣ��򴴽�Ŀ¼
      if not os.path.isdir(local_path):
        os.makedirs(local_path)
      #����ftpĿ¼����ʼ�ݹ��ѯ
      self.conn.cwd(ftp_path)
      ftp_files = self.conn.nlst()
      for file in ftp_files:
        local_file = os.path.join(local_path, file)
        #���file ftp·����Ŀ¼��ݹ��ϴ�Ŀ¼������Ҫ�ٽ��г�ʼ��begin�ı�־�޸�ΪFalse��
        #���file ftp·�����ļ���ֱ���ϴ��ļ�
        if self._is_ftp_dir(file):
          self.get_dir(file,local_file,False)
        else:
          self.get_file(file,local_file)
      #�����ǰftpĿ¼�ļ��Ѿ�������Ϸ�����һ��Ŀ¼
      self.conn.cwd( ".." )
      return
    else:
      print 'ERROR:The dir:%s is not exist' %ftp_path
      return
 
  def put_dir(self,local_path,ftp_path='.',begin=True):
    ftp_path = ftp_path.rstrip('/')
    #������Ŀ¼����ʱ�ϴ�
    if os.path.isdir(local_path):      
      #�ϴ���ʼ�������������ftp·����������Ҫ������ͬʱ�����ص�Ŀ¼����ڸ�����ftpĿ¼�¡�
      #����Ŀ¼���ļ���ŵ�·��Ϊftp_path=ftp_path+os.path.basename(local_path)
      #���磺�������ļ���a�ϴ���ftp��a/bĿ¼�£��򱾵�aĿ¼�µ��ļ����ϴ���ftp��a/b/aĿ¼��
      if begin:        
        if not self._is_ftp_dir(ftp_path):
          self.conn.mkd(ftp_path)
        ftp_path=os.path.join(ftp_path,os.path.basename(local_path))          
      #���ftp·������Ŀ¼���򴴽�Ŀ¼
      if not self._is_ftp_dir(ftp_path):
        self.conn.mkd(ftp_path)
 
      #���뱾��Ŀ¼����ʼ�ݹ��ѯ
      os.chdir(local_path)
      local_files = os.listdir('.')
      for file in local_files:
        #���file����·����Ŀ¼��ݹ��ϴ�Ŀ¼������Ҫ�ٽ��г�ʼ��begin�ı�־�޸�ΪFalse��
        #���file����·�����ļ���ֱ���ϴ��ļ�
        if os.path.isdir(file):          
          ftp_path=os.path.join(ftp_path,file)
          self.put_dir(file,ftp_path,False)
        else:
          self.put_file(file,ftp_path)
      #�����ǰ����Ŀ¼�ļ��Ѿ�������Ϸ�����һ��Ŀ¼
      os.chdir( ".." )
    else:
      print 'ERROR:The dir:%s is not exist' %local_path
      return
if __name__ == '__main__':
  ftp = FTPSync('192.168.1.110')
  ftp.login('test','test')
  #�ϴ��ļ�����������
  #ftp.put_file('111.txt','a/b')
  #�ϴ��ļ���������
  #ftp.put_file('111.txt','a/112.txt')
  #�����ļ�����������
  ftp.get_file('/a/111.txt',r'D:\\')
  �����ļ���������
  #ftp.get_file('/a/111.txt',r'D:\112.txt')
  #���ص��Ѿ����ڵ��ļ���
  #ftp.get_dir('a/b/c',r'D:\\a')
  #���ص������ڵ��ļ���
  #ftp.get_dir('a/b/c',r'D:\\aa')
  #�ϴ����Ѿ����ڵ��ļ���
  ftp.put_dir('b','a')
  #�ϴ��������ڵ��ļ���
  ftp.put_dir('b','aa/B/')