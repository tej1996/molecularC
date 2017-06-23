#!/usr/bin/python

import os,sys,socket,time,subprocess

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000

options='''

!! Welcome to Molecular Cloud Platform !! 
  -------------------------------------

Choose the desired option as required:

1. Ask for new storage (less than available size)
2. Ask for any amount of storage (Thin Provisioning)
3. Extend existing storage
'''

print options

opt=raw_input()

if opt=="1":
	execfile('client/staas/new_storage_fixed.py')
elif opt=="2":
	execfile('client/staas/new_storage_bulk.py')
elif opt=="3":
	execfile('client/staas/extend_exist_storage.py')
else:
	print "Incorrect Input!"
