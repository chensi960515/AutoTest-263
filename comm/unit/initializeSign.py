#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
*****************************
@project:
@author     : chensi
@file       : initializeSign.py
@time       : 2023/6/9 23:53
@msg        : 
******************************
"""
import logging
import time
import json
import os
from json import JSONDecodeError
from config import PAGE_DIR, PROJECT_NAME, API_CONFIG
from comm.unit import apiSend, readRelevance, replaceRelevance
from comm.utils import readYaml

