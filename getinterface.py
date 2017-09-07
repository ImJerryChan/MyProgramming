#!/usr/bin/env python
# coding:utf-8

"""
Script to get the matching interface or ip
author: Jerry Chan
time: 2017-9-7 16:51:11
"""

#build_in
import sys

#third_party
import psutil

def get_ip_addr(option):
	info = psutil.net_if_addrs()
	result = []
	for interface, netinfo in info.items():
		if interface == option:
			for netinfos in netinfo:
				if netinfos[0] == 2:
					result = netinfos[1]
					break
			break
	return result

def get_interface(option):
	info = psutil.net_if_addrs()
	result = []
	break_point = 0
	for interface, netinfo in info.items():
		for netinfos in netinfo:
			if netinfos[1] == option:
				result = interface
				break
	return result

def Useage():
	print " Please Useage:\n   ",__file__,"-i interface\n or",__file__,"-I ip_address"
	sys.exit()
	
if __name__ == '__main__':
	try:
		script, branch, option = sys.argv
	except ValueError:
		Useage()
		
	if branch == "-i":
		ip = get_ip_addr(option)
		tell = ip if ip else "NOT FOUND! %s" % option
		print tell
	elif branch == "-I":
		interface = get_interface(option)
		tell = interface if interface else "NOT FOUND! %s" % option
		print tell
	else:
		Useage()

