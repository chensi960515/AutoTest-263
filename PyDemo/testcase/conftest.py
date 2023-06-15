# -*- coding: utf-8 -*-
# @Time : 2023/6/13 10:09
# @Author : chensi
# @File : conftest.py
# @Project : AutoTest-263
import json
import time
import allure
import pytest
import logging
from config import API_CONFIG, ING_CONFIG
from urllib.parse import urlencode
from comm.utils.readYaml import read_yaml_data, write_yaml_file
from comm.utils.buildSign import timestamp, start_time, end_time
from comm.utils.buildSign import get_sign_string, init_request_string, setSha256
from comm.unit.initializePremise import init_premise
from comm.unit.apiSend import send_request
from comm.unit.checkResult import check_result


@pytest.fixture(scope='function')
def init_sign(request):
    print("执行测试用例前置")
    yaml_path = request.param
    case_data = read_yaml_data(yaml_path)
    aconfig = read_yaml_data(API_CONFIG)
    uri = ''
    # logging.info(len(case_data['test_case']))

    if str(case_data['test_info']['method']).upper() == "GET":
        request_data = case_data['test_case'][0]['parameter']
        # timestamp 放在yaml里面好取但是不好重新赋值，因为真正请求时的timestamp要确保唯一
        request_data['timestamp'] = timestamp
        print(request_data['timestamp'])
        # 获取用例数据中,sign需要的参数
        # request_sign_data = case_data['test_case'][0]['sign_params']
        # logging.info('request_sign_data===' + str(request_sign_data))
        logging.info('request_data===' + str(request_data))

        # 生成sign
        sign_str = get_sign_string(request_data)
        sign = setSha256(init_request_string(sign_str, aconfig['PyDemo']['Appkey']))
        logging.debug('sign ================ ' + sign)
        uri = "sign=" + sign + "&timestamp=" + str(timestamp) + urlencode(get_sign_string(request_data))

        params = {}
        params = case_data['test_case'][0]['parameter']
        params['sign'] = sign
        params['timestamp'] = str(timestamp)
        write_yaml_file(ING_CONFIG, params)



    elif str(case_data['test_info']['method']).upper() == "POST":
        request_data = case_data['test_case'][0]['parameter']
        # 获取用例数据中,sign需要的参数
        # request_sign_data = case_data['test_case'][0]['sign_params']
        # logging.info('request_sign_data===' + str(request_sign_data))
        logging.info('request_data===' + str(request_data))

        # 生成sign
        sign_str = get_sign_string(request_data)
        sign = setSha256(init_request_string(sign_str, aconfig['PyDemo']['Appkey']))
        logging.debug('sign ================ ' + sign)
    else:
        pass

    yield uri
    print("执行测试用例后置")
