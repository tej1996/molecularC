#!/usr/bin/python

import getpass, socket,time, sys

#socket connection between server & client
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

print "!!Login Here!!"

#Username for client login @ server
username = raw_input("Username: ")

#password for client user
password = getpass.getpass("Password: ")

#send credentials to server
sock.sendto(username,(SERVER_IP,SERVER_PORT))
sock.sendto(password,(SERVER_IP,SERVER_PORT))

#setting sys arguments variable
sys.argv.append(username)
sys.argv.append(password)

if sock.recvfrom(100)[0]=="1":
	print "Successful!"
	os.system('tput clear')
	execfile('client/dashboard-client.py')	
else: 
	print "Wrong Username or password!"
	time.sleep(2)	
	exit()




