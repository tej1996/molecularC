#!/usr/bin/python

import os,sys,socket,time

os.system('tput clear')

w_msg='''
!! Welcome to Molecular Cloud Platform !! 
  -------------------------------------
*Services Provided:
+ SAAS
+ STAAS
+ IAAS
'''

print w_msg
print "Loading",

for i in range(3):
    time.sleep(0.5)
    sys.stdout.write(".")
    sys.stdout.flush()

print ""
os.system('tput clear')
execfile('client/login-client.py')
