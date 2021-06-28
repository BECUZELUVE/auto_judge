#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_config.py
@IDE    ：PyCharm
@Author ：Icey
@Desc   ：
'''
from configparser import ConfigParser
import os

from Common.handle_path import config_dir

class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding='utf-8')

file_path = os.path.join(config_dir,"answer_config.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    print(conf.get("Q1","input_1"))
