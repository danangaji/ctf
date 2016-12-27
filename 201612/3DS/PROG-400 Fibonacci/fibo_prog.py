#!/usr/bin/python

import socket
import re
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('54.175.35.248',8000))

def sumiteration(N):

str1 =  sock.recv(2048)
print str1
arrnum = re.findall(r'\d+', str1)
print arrnum[-1]
sock.send(arrnum[-1] + '\n')
str3 = sock.recv(1024)
print str3


sumiteration
