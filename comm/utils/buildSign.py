# -*- coding: utf-8 -*-
# @Time : 2023/6/14 18:03
# @Author : chensi
# @File : buildSign.py
# @Project : AutoTest-263
import json
import copy

json_obj = {'title': '44444', 'mode': 0, 'defalut_streaming_source': 0, 'is_auto_live': True,
            'pull_stream_url': 'rtmp://testextlive.link263.com:19351/cv_live/1547510535023497313#MKYObFjE?auth_key=1973150237817-1547510535023497313-d36731488d959eedaedd3ad4757b7288',
            'is_many_streaming': False, 'is_ultra_hd': False, 'master_control_mode': 0, 'start_time': '1686625781',
            'end_time': '1786625781', 'host_password': 'HPYEDC', 'guest_password': 'ZWOB5A',
            'assistants_password': '', 'password': 'KPii40', 'live_time_delay': 1, 'video_source_ratio': 0,
            'is_auto_recording': None, 'is_join_voip': {},
            'record_resolution': {'is_record_resolution_hd': True, 'is_record_resolution_ld': True,
                                  'is_record_resolution_ud': False}}


# 去除空参数
def delete_null(obj):
    new_obj = copy.copy(obj)
    del_str = ['NONE', 'NULL']

    for key, value in obj.items():
        if str(value) == '{}' or str(value) == '()' or str(value) == '[]':
            del new_obj[key]
        elif len(str(value)) == 0:
            del new_obj[key]
        elif str(value).upper() in del_str:
            del new_obj[key]
    print(new_obj)
    return new_obj


# 去除appId sign tag 参数

# 按照字典排序

# 连接参数名和参数值

# 首位添加Appkey

# 计算加密MD5

delete_null(json_obj)
