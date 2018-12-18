#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import string
from sys import argv
from email.mime.text import MIMEText #导入MIMEText类
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def mail():
	HOST = "smtp.126.com" #定义smtp主机
	SUBJECT = "test-smtp" #定义邮件主题
	TO = "datasec360@126.com" #定义邮件收件人
	FROM = "datasec360@126.com" #定义邮件发件人
	'''
	text = "python test mail" #邮件的内容
	BODY=string.join(( #组装sendmail方法的邮件主体内容，各段以"\r\n"进行分隔
  	"From:%s" %FROM,
  	"To:%s" %TO,
  	"Subject:%s"%SUBJECT,
  	"",
  	text
	),"\r\n")
	'''
	message = MIMEMultipart()
	message['From'] = "datasec360@126.com"
	message['To'] = "datasec360@126.com"
	message['Subject'] = "test-smtp"

	with open('../download/index.html','r') as f:
    		content = f.read()

	part1 = MIMEText(content,'html','utf-8')

	with open('../download/file','r')as h:
    		content2 = h.read()

	part2 = MIMEText(content2,'plain','utf-8')

	part2['Content-Type'] = 'application/octet-stream'

	part2['Content-Disposition'] = 'attachment;filename="file"'

	with open('../download/att.png','rb')as fp:
    		picture = MIMEImage(fp.read())

    		picture['Content-Type'] = 'application/octet-stream'
    		picture['Content-Disposition'] = 'attachment;filename="att.png"'

	message.attach(part1)
	message.attach(part2)
	message.attach(picture)
   	try:
		server = smtplib.SMTP() #创建一个SMTP对象
		server.connect(HOST,"25") #通过connect方法连接smtp主机
		#server.starttls() #启动安全传输模式
		#server = smtplib.SMTP_SSL(HOST)
		server.login("datasec360@126.com","Aa123456") #邮件账户登录校验
		#server.sendmail(FROM,TO,BODY) #邮件发送
		server.sendmail(FROM,TO,message.as_string())
		server.quit() #断开smtp连接
		return True
	except smtplib.SMTPException as e:
		print('error',e)
		return False


if __name__ == '__main__':

    script= argv
    ret=mail()

    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
