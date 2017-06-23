#!/usr/bin/python

import os,sys,socket,time,subprocess

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

#client username and password
username=sys.argv[1]
password=sys.argv[2]

options='''

!! Welcome to Molecular Cloud Platform !! 
  -------------------------------------

Choose the desired option as required: 

1. Run Firefox
2. Run VLC (Play your movie/music)
3. Run Calculator
4. Run OpenOffice 
5. Take Screenshot
6. Run Webcam

'''

print options

opt=raw_input()

if opt=="1":
	execfile('client/saas/firefox.py')
elif opt=="2":
	execfile('client/saas/vlc.py')
elif opt=="3":
	execfile('client/saas/calculator.py')
elif opt=="4":
	execfile('client/saas/openoffice.py')
elif opt=="5":
	execfile('client/saas/screenshot.py')
elif opt=="6":
	execfile('client/saas/webcam.py')
else:
	print "Incorrect Input!"
