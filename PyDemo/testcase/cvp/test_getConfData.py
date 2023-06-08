#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : test_getConfData.py
@time       : 2023/6/8 22:49
@msg        : 
******************************
"""

import os
import allure
import pytest
import logging
from comm.utils.readYaml import read_yaml_data
from comm.unit.initializePremise import init_premise
from comm.unit.apiSend import send_request
from comm.unit.checkResult import check_result

file_path = os.path.realpath(__file__).replace('\\', '/')
case_yaml = file_path.replace('/testcase/', '/page/').replace('.py', '.yaml')
test_case = read_yaml_data(case_yaml)

print("1111")
logging.info(file_path)
logging.info("*" * 150)
logging.info(case_yaml)
logging.info("*" * 150)
logging.info(test_case)


@allure.feature(test_case["test_info"]["title"])
class GetConfData:

    @pytest.mark.parametrize("test_case", test_case["test_case"])
    @allure.story("test_initCanSelInfo")
    def test_getConfData(self, test_case):
        # 初始化请求：执行前置接口+替换关联变量
        test_info, test_case = init_premise(test_case["test_info"], test_case, case_yaml)
        # 发送当前接口
        code, data = send_request(test_info, test_case)
        # 校验接口返回
        check_result(test_case, code, data)
