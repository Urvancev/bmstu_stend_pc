import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9010))
data = ""
#time.sleep(30)
while data != 'stop':
	s.send('B')
	time.sleep(0.2)
	data = s.recv(1024)
	if data:
		buf = ''
		data = bytearray(data)
		print "len data = ",len(data)
		for i in range(0,len(data),1):
			buf += str(data[i])+' '
		print "data = ",buf
	else:
		print "no data"
		s.close()
		break
s.close()
