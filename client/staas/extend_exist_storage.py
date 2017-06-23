#!/usr/bin/python

import getpass, socket,time, sys,os,commands

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

drive_name=raw_input("Enter the drive name: ")
drive_size=raw_input("Enter the drive size to be extended(in MB : eg. 1000,500, any size):")

sock.sendto(drive_name,(SERVER_IP,SERVER_PORT))
sock.sendto(drive_size,(SERVER_IP,SERVER_PORT))

while True:
	response = sock.recvfrom(15)
	result = response[0]
	if result == "success" or result =="error":
		break
	elif result == "insufficient":
		print "Sorry, unable to extend due to insufficient storage!"
		break

if   result == "success" :
	print "Drive named "+drive_name+" is resized!"

else  :
	print   "Error in resizing drive!"

