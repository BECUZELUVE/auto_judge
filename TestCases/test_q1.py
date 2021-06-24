#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> test_q1.py
@IDE    ：PyCharm
@Author ：Icey
@Date   ：2021/6/24 22:22
@Desc   ：
'''

import unittest
from ddt import ddt,data

from Common.handle_requests import send_requests
from Common.handle_input import judge_dict

dic = judge_dict("Q1",3)
input_datas = list(dic.keys())

@ddt
class TestQ1(unittest.TestCase):

    @data(*input_datas)
    def test_q1(self,input_data):
        url = 'https://eduexam.codemao.cn/edu/exams/works/wood?code=sce6Brsz3btYKNWSrZ1WfpbayQ0yXlAKwmL9cKhwulMA5U3q7JZasnGQ9Jm/Mu+kxxjyIkdMW4uH+3IQS2Np8g'
        exec(send_requests(url,input_data))