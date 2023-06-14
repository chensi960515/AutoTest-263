# -*- coding: utf-8 -*-
# @Time : 2023/6/13 10:09
# @Author : chensi
# @File : conftest.py
# @Project : AutoTest-263
import json
import os
import allure
import pytest
import logging
from comm.utils.readYaml import read_yaml_data
from comm.unit.initializePremise import init_premise
from comm.unit.apiSend import send_request
from comm.unit.checkResult import check_result


# 排序

@pytest.fixture(scope='function')
def init_sign(request):
    print("执行测试用例前置")
    yaml_path = request.param
    case_data = read_yaml_data(yaml_path)
    print(case_data)
    # logging.info(len(case_data['test_case']))

    if str(case_data['test_info']['method']).upper() == "GET":
        pass
    elif str(case_data['test_info']['method']).upper() == "POST":
        request_data = case_data['test_case'][0]['params']
        # 获取用例数据中,sign需要的参数
        request_sign_data = case_data['test_case'][0]['sign_params']
        logging.info('request_sign_data===' + str(request_sign_data))
        logging.info('request_data===' + str(request_data))
    else:
        pass

    yield
    print("执行测试用例后置")


def
