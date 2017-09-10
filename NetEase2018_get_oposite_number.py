#!/usr/bin/env python
#coding = utf-8

"""
##网某易2018校招笔试题##
问题描述：为了得到一个数的“相反数”，我们将这个数字顺序颠倒，然后再加上原先得到的“相反数”。例如为了得到1325的“相反数”，首先我们将该数的数字顺序电刀，我们得到5231之后再加上原先的数，我们得到5231+1325=6556.如果点到后的数字有前缀零，则前缀零将会被忽略。例如n=100，颠倒之后是1，结果为101.
"""
#build_in
import sys

def convert_num(num):
    num = int(str(num)[::-1])
    def zero_exist(num):
        num = str(num)
        length = len(num)
        for i in range(1, length + 1):
            if num[i-1] == 0:
                num[i-1].pop()
            else:
                break
        return int(num)
    zero_exist(num)
    return num

if __name__ == '__main__':
    num = raw_input("Please enter a number:")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input, Please enter a number!")
        sys.exit()
    temp = num
    num = convert_num(num)
    result = num + temp
    print("The result is %d") % result
