#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : writeCase.py
@time       : 2023/6/7 23:21
@msg        : 生成测试脚本
******************************
"""

import os
from config import ROOT_DIR
from comm.script.writeCaseYml import write_case_yaml, read_yaml_data
temp_file = ROOT_DIR+'config/test_template.py'