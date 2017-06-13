#!/usr/bin/python

import getpass, socket,time, sys

print "!!Login Here!!"

#Username for user add @ server
username = raw_input("Username: ")

#password for user
password = getpass.getpass("Password: ")

#socket connection for add user @ server
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

sock.sendto(username,(SERVER_IP,SERVER_PORT))
sock.sendto(password,(SERVER_IP,SERVER_PORT))

if sock.recvfrom(100)[0]=="1":
	print "Successful!"
	execfile('client/saas.py')
else: 
	print "Wrong Username or password!"
	time.sleep(2)	
	exit()




