# coding:utf-8
from __future__ import unicode_literals
__author__ = 'the5fire'  # date: 2015-09-21
import select
from Queue import Queue
from model import User, _db  # 写入数据要用
class ChatRoom(object):
    client_sockfds = Queue()
    users = {}

    def chatroom(self, sockfd, addr):
        print sockfd, addr
        # 把sockfd放到队列中
        self.client_sockfds.put(sockfd)
        # 登录前阶段
        user = self.pre_login(sockfd, addr)
        # 广播
        self.broadcast(user, sockfd)


    def create_user(self, sockfd, addr):
        # 这句啥意思
        key = repr(addr)
        try:
            user = self.users[key]
        except KeyError:
            # 这是一个用户名密码为None的空user
            user = User(None, None, sockfd, addr)
            self.users[key] = user
        return user


    def handle_login(self, user, sockfd):
        sockfd.sendall('Please Input Your (Username Password)')
        command = sockfd.recv(1024)
        username, password = command.split(' ')
        # 为空user赋值
        user.username = username
        user.password = password
        # 调用login方法
        if not user.login():
            sockfd.sendall('Wrong Password!\nWhat You Want To Do?(login/registe/exit)')
            return None
        return user


    def handle_register(self, user, sockfd):
        sockfd.sendall('Please Input Your (Username Password)')
        command = sockfd.recv(1024)
        username, password = command.split(' ')
        # 为空user赋值
        user.username = username
        user.password = password
        print user.username, user.password
        # 调用register方法
        if not user.register():
            sockfd.sendall('Username Has Already Exist!\nWhat You Want To Do?(login/registe/exit)')
            return None
        return user


    FUNC_MAP = {
        'login': handle_login,
        'register': handle_register,
    }


    def pre_login(self, sockfd, addr):
        sockfd.sendall('Welcome Chating Room(login/register/exit):')
        # 这是一个用户名密码为None的空user
        user = self.create_user(sockfd, addr)
        
        # 注册登录部分
        while not user.status:
        #while True:
            data = sockfd.recv(1024)  # 等待用户输入
            command = data.strip()
            print command, 'recv'
            # 为什么执行到这里就停下来了
            try:
                command = command.encode('utf-8', 'ignore')
            except Exception:
                pass  # 不需要编码
            try:
                handler = self.FUNC_MAP[command]
                print handler
                user = handler(self, user, sockfd)
                # 奇怪的用法↑↑↑ 去掉self会报错
                # user = self.handle_register(user, sockfd)
                return user
            except KeyError:
                sockfd.sendall('Command Not Found! Please Input Again!(login/registe/exit)')
                break


    def broadcast(self, user, sockfd):
        user.sockfd.sendall('Login Success!')
        rlist = [user.sockfd,]
        while True:
            read_list, write_list, error_list = select.select(rlist , [], [])
            command = rlist[0].recv(1024)
            for i in range(self.client_sockfds.qsize()):
                sockfd = self.client_sockfds.get()
                if sockfd != user.sockfd:
                    sockfd.sendall('[%s] say: %s' % (user.username, command))
                # 发送完，放回去
                self.client_sockfds.put(sockfd)
