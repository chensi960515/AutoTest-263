#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: __init__.py.py
@time: 2022/10/20  22:44
"""
from comm.utils.readYaml import read_yaml_data
import os

# 获取主目录路径
ROOT_DIR = str(os.path.relpath(__file__)).split('config')[0].replace('\\', '/')

# 获取配置文件路径
API_CONFIG = ROOT_DIR+'config/apiConfig.yaml'
RUN_CONFIG = ROOT_DIR+'config/runConfig.yaml'
DB_CONFIG = ROOT_DIR+'config/dbConfig.yaml'
ING_CONFIG = ROOT_DIR+'config/local.yaml'


# 获取运行配置信息
RC = read_yaml_data(RUN_CONFIG)
INTERVAL = RC['interval']
PROJECT_NAME = RC['project_name']

# 接口数据目录(.chlsj文件)
DATA_DIR = ROOT_DIR+PROJECT_NAME+'/data'
# 测试数据目录(test.yaml)
PAGE_DIR = ROOT_DIR+PROJECT_NAME+'/page'
# 测试脚本目录(test.py)
TEST_DIR = ROOT_DIR+PROJECT_NAME+'/testcase'
# 测试报告目录(xml|html)
REPORT_DIR = ROOT_DIR+PROJECT_NAME+'/report'
