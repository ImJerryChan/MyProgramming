#!/bin/bash
# coding: UTF-8
#Script to get the interface or ip
#Version: 1

#functions
Useage(){
	echo "Please useage:$0 -i interface_name or $0 -I IP_Address"
}

ip_processing(){
	result=`ifconfig|grep -A2 $1|grep inet|head -1|awk '{print $2}'|wc -l`
	if [ ${result} -eq 0 ]
	then
		echo "IP NOT FOUND : $1"
		exit
	fi
}

inter_processing(){
	result=`ifconfig|grep -C1 $1|head -1|awk -F':' '{print $1}'|wc -l`
	if [ ${result} -eq 0 ]
	then
		echo "INTERFACE NOT FOUND : $1"
		exit
	fi
}

#Determine the number of input parameters
if [ $# -ne 2 ]
then
	Useage
	exit
fi

case $1 in
	-i)
		ip_processing $2
		ifconfig|grep -A2 $2|grep inet|head -1|awk '{print $2}'
		;;
	-I)
		inter_processing $2
		ifconfig|grep -C1 $2|head -1|awk -F':' '{print $1}'
		;;
	*)
	Useage
	exit
	;;
esac
