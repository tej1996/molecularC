#!/usr/bin/python

import getpass, socket,time, sys,os

sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.7"
SERVER_PORT=1234

os.system("ssh -X test@"+SERVER_IP+" firefox")

