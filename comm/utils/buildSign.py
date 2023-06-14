# -*- coding: utf-8 -*-
# @Time : 2023/6/14 18:03
# @Author : chensi
# @File : buildSign.py
# @Project : AutoTest-263
import json
import copy
import time
import logging
import hashlib


json_sign = {'appId': 'KQt7wKsK6y', 'sign': '8750d8c20fee8c275efe55ebb850bcd9', 'tag': None,
             'Appkey': 'd0001284fc586944036c2d139c3e7bac', 'timestamp': 1686755631413,
             'webcast_id': 1667211537430888467, 'skip': 0, 'take': 20}


timestamp = round(time.time()*1000)
start_time = timestamp + 1000
end_time = start_time + 100000000


# 去除空参数
# 去除appId sign tag 参数
# 排序
def get_sign_string(obj):
    nobj = {}
    new_obj = copy.copy(obj)
    del_str = ['NONE', 'None', 'NULL']
    del_key = ['sign', 'appId', 'tag', 'Appkey']

    for key, value in obj.items():
        if str(value) == '{}' or str(value) == '()' or str(value) == '[]':
            del new_obj[key]
        elif len(str(value)) == 0:
            del new_obj[key]
        elif str(value).upper() in del_str:
            del new_obj[key]
        elif str(key) in del_key:
            del new_obj[key]
    new_obj['timestamp'] = timestamp
    for key in sorted(new_obj):
        nobj[key] = new_obj[key]
    return nobj


# 连接参数名和参数值
# 首位添加Appkey
def init_request_string(obj, Appkey):
    sign_list = []
    sign_str = ''
    for k, v in obj.items():
        sign_list.append(str(k))
        sign_list.append(str(v))

    # print(sign_list)
    for i in sign_list:
        sign_str = sign_str + str(i)
    sign_str = Appkey + sign_str + Appkey
    logging.info("组装完成的未加密sign字符串为：" + sign_str)
    print(sign_str)
    return sign_str


# 计算加密MD5
def setSha256(obj):
    md5 = hashlib.md5()
    md5.update(obj.encode("utf-8"))
    sign = md5.hexdigest()
    # print('MD5加密前为 ：' + obj)
    # print('MD5加密后为 ：' + sign)
    logging.info("MD5加密后为 ：" + sign)

    return sign




# sign_str = init_request_string(get_sign_string(json_sign), '6d2a41710ee887f0e32d81c02a02f45f')
# setSha256(sign_str)

