#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> main.py
@IDE    ：PyCharm
@Author ：Icey
@Desc   ：
'''

import unittest,os,webbrowser
from BeautifulReport import BeautifulReport

from Common.handle_path import cases_dir,reports_dir

all_cases = unittest.TestLoader().discover(cases_dir)

br = BeautifulReport(all_cases)
br.report("p3考生主观题答题情况","report.html",reports_dir)

# 自动打开浏览器
report_file_path = os.path.join(reports_dir,"report.html")
webbrowser.open(report_file_path)