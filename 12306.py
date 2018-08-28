# coding: utf-8

"""
Train Ticket query via command-line

Usage:
  ticket <fro> <dst> <date> [-gdtkz]

Options:
  -h,--help     显示帮助菜单
  -g            高铁
  -d            动车
  -t            特快
  -k            快速
  -z            直达

Example:
  ticket 广州南 容桂 2018-08-20
  ticket 容桂 广州南 2018-09-21 -dg
"""

# 已实现功能
# 颜色，colorama
# 日期格式，dateutil.parser
# 参数支持，docopt
# 异常处理，待完成

import cons
import json
import urllib.request

from colorama import Fore
# from datetime import datetime , 看看为啥没有用到他
from dateutil.parser import parse
from docopt import docopt
from prettytable import PrettyTable


class TrainDataParse(object):
    headers = '车次 车站 时间 历时 特等座 一等座 二等座 软卧 动卧 硬卧 软座 硬座 无座'.split(' ')

    def __init__(self, train_data, station_dict_rev, train_type_dict):
        self.train_data = train_data
        self.station_dict_rev = station_dict_rev
        self.train_type_dict = train_type_dict

    def parse_data(self, data_list):
        return [
            data_list[3],  # '车次'
            self.get_from_to_station(data_list),   # '出发站-到达站'
            self.get_start_arrive_time(data_list),  # '出发时间-到达时间'
            data_list[10],  # '历时'
            data_list[25] or data_list[32] or '--',  # '特等座'
            data_list[31] or '--',  # '一等座'
            data_list[30] or '--',  # '二等座'
            data_list[23] or '--',  # '软卧'
            data_list[33] or '--',  # '动卧'
            data_list[28] or '--',  # '硬卧'
            data_list[24] or '--',  # '软座'
            data_list[29] or '--',  # '硬座'
            data_list[26] or '--',  # '无座'
        ]

    def colored(self, color, str):
        return ''.join([getattr(Fore, color), str, Fore.RESET])

    def get_from_to_station(self, data_list):
        from_station_telecode = self.station_dict_rev[data_list[6]]
        to_station_telecode = self.station_dict_rev[data_list[7]]
        return '\n'.join([
            self.colored('GREEN', from_station_telecode),
            self.colored('RED', to_station_telecode)
        ])

    def get_start_arrive_time(self, data_list):
        start_time = data_list[8]
        arrive_time = data_list[9]
        return '\n'.join([
            self.colored('GREEN', start_time),
            self.colored('RED', arrive_time)
        ])

    def select_train_type(self):
        selected_train_type_list = []
        if 1 in self.train_type_dict.values():
            for key in self.train_type_dict.keys():
                if self.train_type_dict[key]:
                    selected_train_type_list.append(key)  # 获取选择的类别
        else:
            selected_train_type_list = {'G': 1, 'D': 1, 'T': 1, 'K': 1, 'Z': 1}
        return selected_train_type_list

    def select_train_data(self, train_data_list, selected_train_type_list):
        parsed_train_data_list = []
        if train_data_list[3][0:1] in selected_train_type_list:
            parsed_train_data_list = train_data_list
        return parsed_train_data_list

    def pretty_print(self):
        selected_train_type_list = self.select_train_type()
        if self.train_data:
            table = PrettyTable(self.headers)
            for train_data_row in self.train_data:
                train_data_list = train_data_row.split('|')
                parsed_train_data_list = self.select_train_data(train_data_list, selected_train_type_list)  # 经选择过的信息
                if parsed_train_data_list:
                    table.add_row(self.parse_data(parsed_train_data_list))
            print(table)


class Client(object):
    station_cn_en_cache_dict = {}

    def __init__(self):
        self.arguments = docopt(__doc__, version='12306_v2')
        self.gaotie = self.arguments['-g']
        self.dongche = self.arguments['-d']
        self.tekuai = self.arguments['-t']
        self.kuaisu = self.arguments['-k']
        self.zhida = self.arguments['-z']
        self.from_station = ''
        self.to_station = ''
        self.date = self.arguments['<date>']

    def url_request_action(self, url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
        html = urllib.request.urlopen(req).read().decode('utf-8')
        return html

    def station_dict_get(self):
        if not self.station_cn_en_cache_dict:
            for row in cons.station_names.split('@'):
                if row:
                    temp_list = row.split('|')
                    # 使站名中文名和英文简写对应
                    self.station_cn_en_cache_dict[temp_list[1]] = temp_list[2]
        return self.station_cn_en_cache_dict

    def train_type_choose(self):
        return {
            'G': 1 if self.gaotie else 0,
            'D': 1 if self.dongche else 0,
            'T': 1 if self.tekuai else 0,
            'K': 1 if self.kuaisu else 0,
            'Z': 1 if self.zhida else 0,
        }

    def run(self):
        station_dict = self.station_dict_get()
        station_dict_rev = {v: k for k, v in station_dict.items()}
        self.from_station = station_dict[self.arguments['<fro>']]
        self.to_station = station_dict[self.arguments['<dst>']]
        self.date = parse(self.date).strftime('%Y-%m-%d')  # 就是这个东西
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (self.date, self.from_station, self.to_station)
        html = self.url_request_action(url)
        train_data = json.loads(html)['data']['result']
        train_type_dict = self.train_type_choose()
        TrainDataParse(train_data, station_dict_rev, train_type_dict).pretty_print()


if __name__ == '__main__':
    client = Client()
    client.run()
