#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : startup.py
@time       : 2023/6/7 23:57
@msg        : 
******************************
"""

import os
import sys
import pytest
import logging

if __name__ == '__main__':
    from comm.script import writeLogs, writeCase
    from config import *

    # 开启日志记录(默认logs目录)
    writeLogs.MyLogs(ROOT_DIR + 'logs')

    # 判断运行模式
    if RC['auto_switch'] == 1:
        # 如果扫描路径为空在则取项目page目录
        if not RC['scan_dir']:
            RC['scan_dir'] = PAGE_DIR
        logging.info("根据手工编写用例，自动生成测试脚本，然后运行测试！")
        writeCase.write_case(RC['scan_dir'], auto_yaml=False)

    else:
        logging.info("不开启自动生成测试用例功能，将直接运行测试！")

    logging.info(RC['process'])
    # 定义运行参数
    args_list = ['-vs', TEST_DIR,
                 '-n', str(RC['process']),
                 '--reruns', str(RC['reruns']),
                 '--maxfail', str(RC['maxfail']),
                 '--alluredir', REPORT_DIR + '/xml',
                 '--clean-alluredir',
                 '--disable-warnings']
    # 判断是否开启用例匹配
    if RC['pattern']:
        args_list += ['-k ' + str(RC['pattern'])]
    test_result = pytest.main(args_list)
    logging.info(test_result)
    logging.info(args_list)

    # 生成allure报告
    cmd = 'allure generate --clean %s -o %s ' % (REPORT_DIR + '/xml', REPORT_DIR + '/html')
    logging.info(cmd)
    os.system(cmd)
