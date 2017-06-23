#!/usr/bin/python

import getpass, socket,time, sys,os,commands

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

drive_name=raw_input("Enter the drive name: ")
drive_size=raw_input("Enter the drive size (in MB : eg. 1000,500, any size):")

sock.sendto(drive_name,(SERVER_IP,SERVER_PORT))
sock.sendto(drive_size,(SERVER_IP,SERVER_PORT))

while True:
	response = sock.recvfrom(15)
	result = response[0]
	if result == "success" or result =="error":
		break
	elif result == "exist":
		print "Drive with given name exists, please try again!"
		break
	elif result == "nfserror":
		print "Unable to install nfs (Server Error)!"
		break

if   result == "success" :
	# creating local mount point
	mk_o = commands.getstatusoutput('mkdir   /media/'+drive_name+ ' >/dev/null')
	if mk_o[0]!=0:
		commands.getstatusoutput('rmdir   /media/'+drive_name+ ' >/dev/null')	
		commands.getstatusoutput('mkdir   /media/'+drive_name+ ' >/dev/null')
	
	# installing nfs-utils
	nfs_o = commands.getstatusoutput('yum install nfs-utils -y'+ ' >/dev/null')
	if nfs_o[0]!=0:
		print "Unable to install nfs-utils! The requested drive is created but cannot be mounted to your system!"
		exit() 
	# mounting server's drive locally 
	mnt_o = commands.getstatusoutput('mount  '+SERVER_IP+':/mnt/'+drive_name+'   /media/'+drive_name+ ' >/dev/null')
	if mnt_o[0]!=0:
		commands.getstatusoutput('umount  /media/'+drive_name+ ' >/dev/null')
		commands.getstatusoutput('mount  '+SERVER_IP+':/mnt/'+drive_name+'   /media/'+drive_name+ ' >/dev/null')

	print "Drive named "+drive_name+" is mounted and available for use!"

else  :
	print   "Error in mounting drive!"

