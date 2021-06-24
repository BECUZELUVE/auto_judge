#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_input.py
@IDE    ：PyCharm
@Author ：Icey
@Date   ：2021/6/24 22:06
@Desc   ：
'''

from Common.handle_config import conf


def judge_dict(section,n):
    '''
    读取配置文件中的答案用例，并将输入输出内容按字典形式返回
    :param section: answer_config.ini中的section
    :param n: 答案用例的数量
    :return: 字典。key代表输入内容，value代表输出内容
    '''
    input_datas = []
    output_datas = []
    for i in range(1,n+1):
        input_datas.append(conf.get(section,"input_{}".format(i)))
        output_datas.append(conf.get(section, "output_{}".format(i)))

    dic = dict(zip(input_datas,output_datas))
    return dic

if __name__ == '__main__':
    print(judge_dict("Q1",3))