#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : readRelevance.py
@time       : 2022/10/28  20:20
@msg        : 读取关联值
******************************
"""
import logging
import re


__relevance = []


def get_value(data, value):
    """获取数据中的值

    :param data:
    :param value:
    :return:
    """
    global __relevance
    if isinstance(data, dict):
        for key in data:
            if isinstance(data[key], dict):
                get_value(data[key], value)
            elif isinstance(data[key], list):
                for each in data[key]:
                    if isinstance(each, dict):
                        get_value(each, value)
                else:
                    if key == value:
                        __relevance.append(data[key])
            else:
                if key == value:
                    __relevance.append(data[key])
    elif isinstance(data, list):
        for key in data:
            if isinstance(key, dict):
                get_value(key, value)
    return __relevance

