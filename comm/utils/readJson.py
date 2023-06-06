#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project: 
@author     : chensi
@file       : readJson.py
@time       : 2022/10/20  22:59
******************************
"""
import json


def read_json_data(json_file):
    """
    读取json文件数据

    :param json_file:
    :return:
    """
    with open(json_file, 'r', encoding='utf-8') as js_r:
        return json.load(js_r)


def write_json_file(json_file, obj):
    """
    将obj对象写入json文件

    :param json_file:
    :param obj:
    :return:
    """
    with open(json_file, 'w', encoding='utf-8') as js_w:
        json.dump(obj, js_w, ensure_ascii=False, indent=4)
