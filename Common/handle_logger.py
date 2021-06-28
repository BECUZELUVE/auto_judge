#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_logger.py
@IDE    ：PyCharm
@Author ：Icey
@Desc   ：
'''
import logging,os

from Common.handle_config import conf
from Common.handle_path import logs_dir

class HandleLogger(logging.Logger):
    def __init__(self,file=None):
        # 设置输出级别、输出渠道、输出日志格式
        # super().__init__(name,level)
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # 日志格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行：%(message)s "
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        # 文件渠道
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

# 判断是否需要写入文件
if conf.getboolean('log','file_ok'):
    file_path = os.path.join(logs_dir, conf.get('log','file_name'))
else:
    file_path = None

logger = HandleLogger(file_path)