#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Project -> File   ：003auto_judge -> handle_requests.py
@IDE    ：PyCharm
@Author ：Icey
@Desc   ：
'''
import requests,os
import sys
from subprocess import Popen, PIPE, STDOUT,getstatusoutput

from Common.handle_path import datas_dir


def send_requests(url,input_data):
    '''

    :param url: 学生考卷链接
    :param input_data: 字符串。要替换的数据
    :return:
    '''
    res = requests.get(url).text
    print(res)
    res = res.replace("input()",input_data)
    # code = compile(res,"<string>","exec")
    # print(code)

    # 将替换测试数据写入到临时代码文件中方便后续运行
    with open(os.path.join(datas_dir,"temp.py"),"w",encoding='utf-8') as f:
        f.write("# -!- coding: utf-8 -!-\nimport sys,io\nsys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')\n"+res)
    # try:
    p = Popen([sys.executable, os.path.join(datas_dir, "temp.py")], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    # 查看交互的内容数据
    # print(p.communicate())

    try:
        # 这行代码是将另外一个程序的输出结果获取到，
        content = p.communicate(timeout=5)[0]
        if p.poll() == 0: # 子进程退出状态码，0代表正常退出，其他代表不正常
            # 原来是 bytes类型的数据，需要将获取到的内容进行解码
            content = content.decode("gbk")
            return content.strip()
    except: # 如果子进程中有死循环就会运行超时，kill掉
        p.kill()




if __name__ == '__main__':
    url='https://eduexam.codemao.cn/edu/exams/works/wood?code=sce6Brsz3btYKNWSrZ1WfpbayQ0yXlAKwmL9cKhwulNiF226D289RL8/aOq0KxURxxjyIkdMW4uH+3IQS2Np8g'
    # url = 'https://eduexam.codemao.cn/edu/exams/works/wood?code=sce6Brsz3btYKNWSrZ1WfpbayQ0yXlAKwmL9cKhwulMA5U3q7JZasnGQ9Jm/Mu+kxxjyIkdMW4uH+3IQS2Np8g'
    send_requests(url,"17")