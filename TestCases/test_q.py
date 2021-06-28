#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> test_q1.py
@IDE    ：PyCharm
@Author ：Icey
@Desc   ：
'''

import unittest,os
from ddt import ddt,data

from Common.handle_excel import HandleExcel
from Common.handle_requests import send_requests
from Common.handle_data import judge_dict

from Common.handle_logger import logger
from Common.handle_path import datas_dir,output_datas_dir

file_path = os.path.join(datas_dir, "answer_datas.xlsx")
# file_path = os.path.join(datas_dir, "temp_data.xlsx")
out_file_path = os.path.join(output_datas_dir, "output_datas.xlsx")
excel = HandleExcel(file_path,'P3考生成绩明细')
infos = excel.read_all_datas()
excel.close_file()




@ddt
class TestQ1(unittest.TestCase):
    @classmethod
    def tearDownClass(cls) -> None:
        # 用例执行完毕后将结果导出在Outputs/datas/output_datas.xlsx
        excel.output_excel(infos,out_file_path)
        excel.close_file()

    @data(*infos)
    def test_q1(self,info):
        n = 3  # 答案中测试用例的数量
        dic = judge_dict("Q1", n)
        input_datas = list(dic.keys())
        url = info["第21题"]
        if url != "未作答":
            info["第21题分数"] = int(info["第21题分数"])+1
            for i in range(n):
                res = send_requests(url,input_datas[i])
                logger.info("考生id:{}的代码，用例{}的运行结果为：{}，期待运行结果为：{}".format(info["id"],i,res,dic[input_datas[i]]))
                try:
                    self.assertEqual(str(res).strip(),str(dic[input_datas[i]]).strip())
                except Exception as e:
                    logger.info("异常原因为：{}".format(e))
                    raise
                else:
                    info["第21题分数"] = int(info["第21题分数"])+3
        else:
            logger.info("考生未作答")

    @data(*infos)
    def test_q2(self, info):
        n = 3  # 答案中测试用例的数量
        dic = judge_dict("Q2", n)
        input_datas = list(dic.keys())
        url = info["第22题"]
        if url != "未作答":
            info["第22题分数"] = int(info["第22题分数"]) + 1
            for i in range(n):
                res = send_requests(url, input_datas[i])
                logger.info("考生id:{}的代码，用例{}的运行结果为：{}，期待运行结果为：{}".format(info["id"], i, res, dic[input_datas[i]]))
                try:
                    self.assertEqual(str(res).strip(),str(dic[input_datas[i]]).strip())
                except Exception as e:
                    logger.info("异常原因为：{}".format(e))
                    raise
                else:
                    info["第22题分数"] = int(info["第22题分数"]) + 3
        else:
            logger.info("考生未作答")

    @data(*infos)
    def test_q3(self, info):
        n = 3  # 答案中测试用例的数量
        dic = judge_dict("Q3", n)
        input_datas = list(dic.keys())
        url = info["第23题"]
        if url != "未作答":
            info["第23题分数"] = int(info["第23题分数"]) + 1
            for i in range(n):
                res = send_requests(url, input_datas[i])
                logger.info("考生id:{}的代码，用例{}的运行结果为：{}，期待运行结果为：{}".format(info["id"], i, res, dic[input_datas[i]]))
                try:
                    self.assertEqual(str(res).strip(),str(dic[input_datas[i]]).strip())
                except Exception as e:
                    logger.info("异常原因为：{}".format(e))
                    raise
                else:
                    info["第23题分数"] = int(info["第23题分数"]) + 3
        else:
            logger.info("考生未作答")






