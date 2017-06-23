#!/usr/bin/python

import socket,os

#socket connection between server & client
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000
sock.bind(("",8000))

while True:
	
	#  dn_data  will receive  drive name to be extended
	dn_data = sock.recvfrom(20)
	d_name = dn_data[0]

	#  es_data  will receive size to be extended 
	es_data = sock.recvfrom(10)
	extend_size = es_data[0]
	
	# client_ip will contain client's ip address  
	client_ip = es_data[1][0]

	# extending the partition size 
	lv_o = os.system('lvextend --size +'+extend_size+'M /dev/m_vol_grp/'+d_name)
	if lv_o!=0:
		sock.sendto("insufficient",es_data[1])
		break

	# formatting client's extended partition drive with ext4  
	fm_o = os.system('resize2fs /dev/m_vol_grp/'+d_name)
	if fm_o==0:
		sock.sendto("success",es_data[1])
	else:
		sock.sendto("error",es_data[1])
