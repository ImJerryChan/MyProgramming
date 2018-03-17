#!/usr/bin/env python
# coding: utf-8

"""
##京某东2018笔试题##
问题描述：有一个无限长数字序列:1,2,3,3,3,4,4,4,4....
"""

def create_list(num):
	list = []
	for i in range(1, num + 1):
		list.append(num)
	return list
	
#这里是我笔试的时候做错的，那时候脑子抽了，居然用了nlist.index()，那不是取编号为index的值啊啊，是取这个这个值所对应的index啊！！！血的教训
#def query_number_index(index, nlist):
#	result = nlist.index(index + 1)
#	return result
	
def query_number_index(index, nlist):
	result = nlist[index - 1]
	return result
	
if __name__ == '__main__':
	num =raw_input("Please input the max number:")
	num = int(num)
	list = []
	for nums in range(1, num + 1):
		nlist = create_list(nums)
		list.extend(nlist)
	print("List create complite!")
	print list
	query_index = raw_input("Please enter the index: ")
	query_index = int(query_index)
	print("Okey, the result of %r is: %r") % (query_index, query_number_index(query_index, list))
