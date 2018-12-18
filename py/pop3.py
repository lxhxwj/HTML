#!/usr/bin/python
# -*- coding: UTF-8 -*-
#_DEBUG=True
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = 'datasec360@126.com'
password = 'Aa123456'
pop3_server = 'pop.126.com'


server = poplib.POP3(pop3_server)

# server.set_debuglevel(1)

print(server.getwelcome())

server.user(email)
server.pass_(password)

print('Messages: %s. Size: %s' % server.stat())

resp, mails, octets = server.list()

print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)


msg_content = '\r\n'.join(lines)

msg = Parser().parsestr(msg_content)

# server.dele(index)

server.quit()
