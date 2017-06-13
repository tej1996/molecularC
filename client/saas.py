#!/usr/bin/python

import os,sys,socket,time

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

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
	execfile('client/firefox.py')
elif opt=="2":
	execfile('vlc.py')
elif opt=="3":
	execfile('calculator.py')
elif opt=="4":
	execfile('openoffice.py')
elif opt=="5":
	execfile('sreenshot.py')
elif opt=="6":
	execfile('webcam.py')
else:
	print "Incorrect Input!"
