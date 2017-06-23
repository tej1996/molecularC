#!/usr/bin/python

import os,sys,socket,time,subprocess

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

options='''

!! Welcome to Molecular Cloud Platform !! 
  -------------------------------------

Choose the desired option as required: 

1. SAAS
2. STAAS

'''

print options

opt=raw_input()

if opt=="1":
	execfile('client/saas.py')
elif opt=="2":
	execfile('client/staas.py')
else:
	print "Incorrect Input!"
