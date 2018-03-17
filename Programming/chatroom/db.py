# coding: utf-8

'''
数据存储结构：
username1 password1
username2 password2
...
'''

from settings import DB_PATH


class StoreError(Exception):
    pass
class DB(object):
    def __init__(self, path=DB_PATH):
        self.data_list = {}
        self.path = path
        # 给我写的话我可能暂时想不到要读里面的内容
        with open(self.path) as f:
            for line in f:
                username, password = line.split(' ')
                self.data_list[username] = line
                # 稍作提示的话，我可能写到这里就结束了
        # self.max_id = max(self.index_lines.keys() or [0])


    def db_data_add(self, username, password):
        print username, password
        username = str(username)
        password = str(password)
        line = username + ' ' + password
        self.data_list[username] = line
        self._store()


    def query_by_username(self, username):
        try:
            line = self.data_list[username]
            print line
        except KeyError:
            return None, None
        return line.split(' ')


    def _store(self):
        # 给我写不会加上try，还有这个raise
        try:
            with open(self.path, 'w') as f:
                for line in self.data_list.values():
                    f.write(line)
        except Exception as e:
            # 检测文件权限
            print '权限为只读，请修改权限'
            raise StoreError(e)
