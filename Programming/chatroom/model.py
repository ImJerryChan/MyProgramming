# coding: utf-8

'''
数据存储结构：
username1 password1
username2 password2
...
'''

from db import DB


_db = DB()


class User(object):
    def __init__(self, username, password, sockfd=None, addr=None, status=None):
        self.username = username
        self.password = password
        self.sockfd = sockfd
        self.addr = addr
        self.status = status


    def login(self):
        real_username, real_password = _db.query_by_username(self.username)
        if self.username == real_username and self.password == real_password:
            self.status = 'online'
            return True
        return False


    def register(self):
        if self.username in _db.data_list.keys():  # 已存在相同username
            return False
        print self.username, self.password
        _db.db_data_add(self.username, self.password)
        self.status = 'online'
        return True
