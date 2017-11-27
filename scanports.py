# coding: utf-8

#多线程端口扫描

import sys
import socket
from mult


#传入参数hostIP,port范围

sPorts = "1-1024"
if len(sys.argv) == 1:
	sHostIP = sys.argv[1]
elif len(sys.argv) == 2:
	sHostIP = sys.argv[1]
	sPorts = sys.argv[2]
else:
	print "输出参数错误"
	print "用法：python scanports.py 10.0.0.2 [1-1024]"
	sys.exit()

socket.setdefaulttimeout(0.5)
ports = []

def scanports(port):
	try:
		s = socket.socket(2,1)
		result = s.connect_ex((sHostIP,port))
		if result == 0:
			print "Port {}:OPEN".format(port)
		s.close()
	except Exception,e:
		print str(e.message)

lstPort = sPorts.split('-')
for i in range(int(lstPort[0]),int(lstPort[1]+1)):
	ports.append(i)

pool ThreadPool(processes = 8)
result_pool = pool.map(scanports,ports)
pool.close()
pool.join()

