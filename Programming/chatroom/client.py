#!/usr/bin/env python
# coding: utf-8

import select
import socket
import sys
import time
from model import User
from threading import Thread

# Client 功能
# 1.监听服务器是否有消息发送过来
# 2.检查用户的输入，如果用户输入某条消息，需要发送到服务器
class Client(Thread):
    def __init__(self):
        # 遵从和服务端一样的协议/IP地址/端口号
        self.sock = socket.socket()
        # 客户端自身启动一个“随机”端口号，并把端口号发给服务端
        # 三次握手开始
        self.sock.connect(('123.207.241.207', 10003))
        self.sock.settimeout(4)
        super(Client, self).__init__()
    def run(self):
        while True:
            rlist = [sys.stdin, self.sock]  # self.sock是和服务器连接的sock
            read_list, write_list, error_list = select.select(rlist , [], [])
            # 当获取到广播，或者是自己写了东西的话
            for sock in read_list:
                # 获取到ChatServer的信息（CHATROOM部分尚未完成）
                if sock == self.sock:
                    try:
                        result = self.sock.recv(1024)
                        print result
                    except socket.timeout:
                        print 'timeout'
                        # Disconnect from chat server
                        sys.exit()
                # 向ChatServer发送数据
                else:
                    msg = sys.stdin.readline()
                    self.sock.sendall(msg)
                    print '<ME> %s' %msg



def main():
    client = Client()
    client.setDaemon(1)  # 功能和.join()基本相反
    client.start()
    while True:
        time.sleep(100)


if __name__ == '__main__':
    main()
