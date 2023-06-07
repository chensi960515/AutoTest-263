#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : __init__.py.py
@time       : 2023/6/7 23:15
@msg        : 
******************************
"""

from config import read_yaml_data, DB_CONFIG, PROJECT_NAME
DC = read_yaml_data(DB_CONFIG)[PROJECT_NAME]

if 'mysql_info' in DC:
    from .queryMysql import MysqlServer
if 'redis_info' in DC:
    from .queryRedis import exec_redis
