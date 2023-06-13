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


@pytest.fixture()
def init_sign(request):
    print("执行测试用例前置")
    case_data = request.param
    logging.info("case_data===" + str(case_data))

    request_data = {}
    if str(case_data['test_info']['method']).upper() == "GET":
        pass
    elif str(case_data['test_info']['method']).upper() == "POST":

    else:
        pass

    yield
    print("执行测试用例后置")
