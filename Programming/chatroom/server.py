# coding:utf-8
__author__ = 'the5fire'
#import logging
import time
import select
import sys
import socket
from threading import Thread
import settings
from chat import ChatRoom
#logger = logging.getLogger(__name__)

# Server功能
# 接收多个客户端的连接
# 从每个客户端读入消息病广播到其它连接的客户端
class ChatServer(Thread):
    def __init__(self, sock):
        self.running = True
        # 下面的socks就是经过绑定协议/IP地址/端口号的socks
        self.sock = sock
        self.room = ChatRoom()
        super(ChatServer, self).__init__()
    def run(self):
        while self.running:
            try:
                # 三次握手，接收到客户端的请求，addr依旧是一个pair
                # sockfd 实质也是一个 sock， 代表服务器和客户端的连接
                sockfd, addr = self.sock.accept()
                self.room.chatroom(sockfd, addr)
            except KeyboardInterrupt:
                self.running = False
            #except Exception as e:
            #    logger.error(e)
            #else:
                # 这里回去的数据要处理一下
                #data = sock.recv(1024)
    @classmethod
    def serve_forever(cls, addr, pool_size=10):  # 这里的addr是一个pair
        # 创建一个socket对象
        sock = socket.socket()
        # 协议什么的
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定本机IP地址和端口号
        sock.bind(addr)
        print 'listening on  %s:%s' % addr
        # 启动监听，服务端建立完成
        sock.listen(1024)
        thread_pool = [cls(sock) for i in range(pool_size)]
        try:
            for thread in thread_pool:
                thread.setDaemon(1)
                thread.start()
            while True:
                # use for captach Keyboard Interrupt
                time.sleep(1000)
        except KeyboardInterrupt:
            sys.exit()


def main():
    ChatServer.serve_forever((settings.HOST, settings.PORT))


if __name__ == '__main__':
    main()
