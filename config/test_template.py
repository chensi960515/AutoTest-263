#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : test_template.py
@time       : 2023/6/7 23:51
@msg        : 测试脚本模板
******************************
"""
import logging
import os
import allure
import pytest
from comm.utils import get_case, read_yaml_data
from comm.unit.initializePremise import init_premise
from comm.unit.apiSend import send_request
from comm.unit.checkResult import check_result
case_path, case_data = get_case(os.path.realpath(__file__))
file_path = os.path.realpath(__file__).replace('\\', '/')
case_yaml = file_path.replace('/testcase/', '/page/').replace('.py', '.yaml')
case_data = read_yaml_data(case_yaml)


@allure.feature(case_data["test_info"]["title"])
class TestTemplate:

    @pytest.mark.parametrize("test_case", case_data["test_case"])
    @allure.story("test_template")
    def test_template(self, test_case):
        # 初始化请求：执行前置接口+替换关联变量
        test_info, test_case = init_premise(case_data["test_info"], test_case, case_path)
        logging.info(test_info)
        # 发送当前接口
        code, data = send_request(test_info, test_case)
        # 校验接口返回
        check_result(test_case, code, data)
