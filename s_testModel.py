import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9000))
data = ""
while data != 'stop':
	s.send('M')
	time.sleep(0.2)
	data = s.recv(1024)
	if data:
		buf = ''
		data = bytearray(data)
		print "len data = ",len(data)
		for i in range(len(data)):
			buf += str(data[i])+' '
		print "Model data = ",buf
	else:
		print "no data"
		s.close()
		break
s.close()
