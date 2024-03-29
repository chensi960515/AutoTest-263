﻿#!/usr/bin/env/python3
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
from comm.utils.buildSign import timestamp, start_time, end_time

file_path = os.path.realpath(__file__).replace('\\', '/')
case_yaml = file_path.replace('/testcase/', '/page/').replace('.py', '.yaml')
case_data = read_yaml_data(case_yaml)
realy_case_data = read_yaml_data(file_path.replace('local.yaml'))

print(str(case_yaml))

case_yaml_path = []
case_yaml_path.append(case_yaml)


@allure.feature(case_data["test_info"]["title"])
class TestRegister:

    @pytest.mark.parametrize('init_sign', case_yaml_path, indirect=True)
    @pytest.mark.parametrize("test_case", case_data["test_case"])
    @allure.story("test_getConfData")
    def test_getConfData(self, test_case, init_sign):
        # uri = init_sign
        logging.info("用例前置请求返回uri地址为 ============ " + init_sign)
        # 初始化请求：执行前置接口+替换关联变量
        test_info, test_case = init_premise(case_data["test_info"], test_case, case_yaml)
        # 发送当前接口
        # test_info['uri'] = uri
        code, data = send_request(test_info, test_case)
        # 校验接口返回
        check_result(test_case, code, data)



