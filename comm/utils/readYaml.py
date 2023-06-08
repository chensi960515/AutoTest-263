#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project: 
@author     : chensi
@file       : readYaml.py
@time       : 2022/10/20  22:51
******************************
"""
import logging


def read_yaml_data(yaml_file):
    """
    读取yaml文件数据

    :param yaml_file: yaml文件地址
    :return:
    """
    import yaml
    with open(yaml_file, 'r', encoding='utf-8') as ya_r:
        return yaml.load(ya_r, Loader=yaml.SafeLoader)


def write_yaml_file(yaml_file, obj):
    """
    将obj对象写入yaml文件中

    :param yaml_file: yaml文件地址
    :param obj: 数据对象
    :return:
    """
    from ruamel import yaml
    with open(yaml_file, 'w', encoding='utf-8') as ya_w:
        yaml.dump(obj, ya_w, Dumper=yaml.RoundTripDumper, allow_unicode=True)
