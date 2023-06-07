#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: 
@author: chensi
@file: __init__.py.py
@time: 2022/10/20  22:44
"""

import os
from comm.utils.readYaml import read_yaml_data


def get_case(file_path):
    case_yaml = file_path.replace('\\', '/').replace('/testcase/', '/page/').replace('.py', '.yaml')
    case_path = os.path.dirname(case_yaml)
    case_data = read_yaml_data(case_yaml)
    return case_path, case_data
