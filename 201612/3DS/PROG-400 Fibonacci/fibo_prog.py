#!/usr/bin/python

import socket
import re
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('54.175.35.248',8000))

def countit(n):
    totaln = 0
    total1 = 0
    total2 = 0
    for i in xrange(1, n+1):
        if i == 1:
            totaln = 0
            total1 = 0
            total2 = 0
        elif i == 2:
            totaln = 2
            total1 = 0
            total2 = 2
        else:
            totaln = total1 + total2 + 2
            total1 = total2
            # Send only last 3 number
            if totaln > 999:
                totaln = totaln - 1000
            total2 = totaln
    return totaln

str1 =  sock.recv(2048)
print str1
arrnum = re.findall(r'\d+', str1)
print arrnum[-1]
sock.send(arrnum[-1] + '\n')
sock.settimeout(10.0)
str3 = sock.recv(1024)
print str3
for i in xrange(1,205):
    if str3.find('Wrong') == -1:
        iterasi = -1
        arrnum3 = re.findall(r'\d+', str3)
        if len(arrnum3) == 0:
            print i
            str3 = sock.recv(1024)
            print str3
        else:
            tohit = int(arrnum3[-1])
            hasil = countit(tohit)
            time.sleep(3)
            tosend = str(hasil)
            sock.send(tosend + '\n')
            print i, tosend, hasil
            str3 = sock.recv(1024)
            print str3
    else:
        break
sock.close

