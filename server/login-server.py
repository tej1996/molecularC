#!/usr/bin/python

import socket,os

#socket connection between server & client
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000
sock.bind(("",8000))

while True:
	#received username and password
	username=sock.recvfrom(100)
	password=sock.recvfrom(100)

	#saves exit code for useradd and password  

	#u=os.system("adduser "+username)
	#p=os.system("echo "+password[0]+"| passwd "+username+" --stdin")

	if username[0]=="test" and password[0]=="123":
		result = "1"
	else:
		result = "0" 

	sock.sendto(result,password[1])

