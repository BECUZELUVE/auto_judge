#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_path.py
@IDE    ：PyCharm
@Author ：Icey
@Date   ：2021/6/24 22:06
@Desc   ：
'''

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(base_dir)

# 测试数据路径
datas_dir = os.path.join(base_dir,"TestDatas")

# 测试用例路径
cases_dir = os.path.join(base_dir,"TestCases")

# 配置文件路径
config_dir = os.path.join(base_dir,"Config")