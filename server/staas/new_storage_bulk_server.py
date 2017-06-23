#!/usr/bin/python

import socket,os

#socket connection between server & client
sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
SERVER_IP="192.168.122.152"
SERVER_PORT=8000
sock.bind(("",8000))

while True:
	
	#  dn_data  will receive  drive  name 
	dn_data = sock.recvfrom(20)
	d_name = dn_data[0]

	#  ds_data  will receive  drive  size 
	ds_data = sock.recvfrom(10)
	d_size = ds_data[0]
	
	# client_ip will contain client's ip address  
	client_ip = ds_data[1][0]

	# creating Logical Volume thin pool by the name of client's drive  
	lv_o = os.system('lvcreate -V'+d_size+'M --name '+d_name+' --thin  m_vol_grp/m_pool1  -y')
	if lv_o!=0:
		sock.sendto("exist",ds_data[1])
		break
	
	# formatting client's drive with ext4  
	os.system('mkfs.ext4   /dev/m_vol_grp/'+d_name)
	
	# creating mount point  
	mk_o = os.system('mkdir   /mnt/'+d_name)
	if mk_o!=0:
		os.system('rmdir   /mnt/'+d_name)
		os.system('mkdir   /mnt/'+d_name)
	
	# mounting drive locally  
	mnt_o = os.system('mount  /dev/m_vol_grp/'+d_name+'  /mnt/'+d_name)
	if mnt_o!=0:
		os.system('umount  /mnt/'+d_name)
		os.system('mount  /dev/m_vol_grp/'+d_name+'  /mnt/'+d_name)
	
	# Starting NFS server configuration  
	nfs_o = os.system('yum  install  nfs-utils  -y')
	if nfs_o!=0:
		sock.sendto("nfserror",ds_data[1])
		break
	
	# making entry in Nfs export file 
	entry="/mnt/"+d_name+"  "+client_ip+"(rw,no_root_squash)"

	# appending this entry var to /etc/exports file 
	file_exp = open('/etc/exports','a+')
	flag_exist=0
	#checking if entry already exists or not	
	for line in file_exp:	
		if entry in line:
			flag_exist=1
			break

	if flag_exist != 1:		
		file_exp.write(entry)
		file_exp.write("\n")
	
	file_exp.close()

	# finally  starting  nfs  service  and service  persistant 
	#os.system('systemctl   restart  nfs-server')
	os.system('systemctl   enable  nfs-server')

	check_nfs_update = os.system('exportfs  -r')

	if  check_nfs_update  ==  0 :
		sock.sendto("success",ds_data[1])

	else :
		sock.sendto("error",ds_data[1])

