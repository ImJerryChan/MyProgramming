#! /usr/bin/env python
# coding: utf-8
# Written By JerryChan
# 2018年3月12日17:07:37

import argparse
import os
import psutil
import shutil
import sys

# dest 的作用是将sys.argv输入的内容把它转换为 dirpath,filename，作为函数使用的参数
# default，如果命令行中没有出现该参数时的默认值。在这里也就是backup_path的默认值
# 详细怎么用，请参考官方文档：http://python.usyiyi.cn/translate/python_278/library/argparse.html
parser = argparse.ArgumentParser(description='python实现升级版rm(在删除之前先备份文件，然后再删除)')
parser.add_argument('-d', '--dir', dest='dirpath', default=None, type=str, help="要删除的目录")
parser.add_argument('-f', '--file', dest='filename', default=None, type=str, help='要删除的文件')
parser.add_argument('-p', '--path', dest='backup_path', default='/tmp/data_bak', type=str, help='备份的路径，默认为/tmp/data_bak')


def is_valid(filename, dirpath):
    '''
    数据有效性校验
    '''
    # 防止两个均存在数据
    if filename and dirpath:
        return 1
    # 防止非文件
    if filename and not dirpath:
        if not os.path.isfile(filename):
            return 2
    # 防止非目录
    if dirpath and not filename:
        if not os.path.isdir(dirpath):
            return 3
    return 0


def rm_ui(filename, dirpath, backup_path):
    '''
    程序UI层
    '''
    if is_valid(filename, dirpath) == 1:
        print "Invalid Input! You can only chose either of the '-d' and '-f'."
    elif is_valid(filename, dirpath) == 2:
        print "%s is not a file" % filename
    elif is_valid(filename, dirpath) == 3:
        print "%s is not a directory" % dirpath
    else:
        choose = raw_input('Mission Remove Will Be Done, Do You Want To Continue? [Y/N] ')
        
        if choose  in ['Y', 'y', 'yes']:
            print 'Mission Ensure!'
            action(filename, dirpath, backup_path)
        elif choose in ['N', 'n', 'no']:
            print 'Delete Mission Abort!'
        else:
            print 'Invalid Choose!'


def action(filename, dirpath, backup_path):
    # 删除目录
    if dirpath and not filename:
        shutil.copytree(dirpath, backup_path)
        print '%s backup success!' %dirpath
        shutil.rmtree(dirpath)
        print '%s remove success!' %dirpath
    # 删除文件
    elif filename and not dirpath:
        shutil.copy2(filename, backup_path)
        print '%s backup success!' %filename
        os.remove(filename)
        print '%s remove success!' %filename
    else:
        print 'Unknown Error Exist!'
        sys.exit()


def main():
    args = parser.parse_args()
    rm_ui(args.filename, args.dirpath, args.backup_path)


if __name__ == '__main__':
    main()
