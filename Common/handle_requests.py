#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_requests.py
@IDE    ：PyCharm
@Author ：Icey
@Date   ：2021/6/24 22:02
@Desc   ：
'''
import requests,os

from Common.handle_path import datas_dir

def send_requests(url,input_data):
    '''

    :param url: 学生考卷链接
    :param input_data: 字符串。要替换的数据
    :return: 字符串。读取到的答案内容
    '''
    res = requests.get(url).text
    res = res.replace("input()",input_data)
    # print(res)
    code = compile(res,"<string>","exec")
    exec(code)
    # result_list = []
    # with open(os.path.join(datas_dir,"temp.txt"),"w") as f:
    #     f.write(str(exec(code)))
    # with open(os.path.join(datas_dir,"temp.txt")) as f:
    #     a = f.read()
    # return a




if __name__ == '__main__':
    url = 'https://eduexam.codemao.cn/edu/exams/works/wood?code=sce6Brsz3btYKNWSrZ1WfpbayQ0yXlAKwmL9cKhwulMA5U3q7JZasnGQ9Jm/Mu+kxxjyIkdMW4uH+3IQS2Np8g'
    print(send_requests(url,"17"))