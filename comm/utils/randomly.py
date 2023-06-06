import string
import random
import datetime
from dateutil.relativedelta import relativedelta


def random_str(str_len):
    """
     从 a-z A-Z 0-9 生成指定数量的随机字符

    :param str_len: 字符串长度
    :return:
    """
    try:
        str_len = int(str_len)
    except ValueError:
        raise Exception("调用随机字符失败，[ %s ]长度参数有误，需要为正整数！！！" % str_len)
    strings = ''.join(random.sample(string.hexdigits, +str_len))
    return strings


def random_int(scope):
    """
     获取随机整数数据
    :param scope:  数据范围
    :return:
    """
    try:
        start_num, end_num = scope.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
    except ValueError:
        raise Exception("调用随机整数失败， [ %s ]范围参数有误！！！" % str(scope))
    if start_num <= end_num:
        number = random.randint(start_num, end_num)
    else:
        number = random.randint(end_num, start_num)
    return number


def random_float(data):
    """
     获取随机浮点数
    :param data: 数组
    :return:
    """
    try:
        start_num, end_num, accuracy = data.split(",")
        start_num = int(start_num)
        end_num = int(end_num)
        accuracy = int(accuracy)
    except ValueError:
        raise Exception("调用随机浮点数失败，[ %s ]范围参数或精度有误！！！" % data)


def random_choice(data):
    """
    获取数组随机值

    :param data: 数组
    :return:
    """
    _list = data.split(",")
    each = random.choice(_list)
    return each


def get_date_mark(now, mark, num):
    """
    生成日期对象使用

    :param now:
    :param mark:
    :param num:
    :return:
    """
    if 'y' == mark:
        return now + relativedelta(years=num)
    elif 'm' == mark:
        return now + relativedelta(months=num)
    elif 'd' == mark:
        return now + relativedelta(days=num)
    elif 'h' == mark:
        return now + relativedelta(hours=num)
    elif 'M' == mark:
        return now + relativedelta(minutes=num)
    elif 'S' == mark:
        return now + relativedelta(seconds=num)
    else:
        raise Exception("日期字段标识 [ %s ]错误，请使用[年y,月m,日d,时h,分M,秒s]标识!" % mark)


def generate_date(expr=''):
    """
    生成日期对象（不含时分秒） or 获取当前日期
    :param expr: 日期表达式， 如； ”d-1“ 表示日期减1
    :return:
    """
    today = datetime.date.today()
    if expr:
        try:
            mark = expr[:1]
            num = int(expr[1:])
        except (TypeError, NameError):
            raise Exception('调用生成日期失败，日期表达式[%s]有误！' % expr)
        return get_date_mark(today, mark, num)
    else:
        return today


def generate_datetime(expr=''):
    """
    生成日期对象 包含时分秒
    :param expr:  日期表达式，如”d-1“ 表示日期减1
    :return:
    """
    now = datetime.datetime.now().replace(microsecond=0)
    if expr:
        try:
            mark = expr[:1]
            num = int(expr[1:])
        except(TypeError, NameError):
            raise Exception('调用生成日期失败，日期表达式[%s]有误！' % expr)
        return get_date_mark(now, mark, num)
    else:
        return now


def generate_timestamp(expr=''):
    """
    获取当前时间戳 13 位
    :param expr:  日期表达式
    :return:
    """
    datetime_obj = generate_datetime(expr)
    return int(datetime.datetime.timestamp(datetime_obj)) * 1000


def generate_guid():
    """
    基于MAC地址 + 时间戳 + 随机数生成GUID
    :return:
    """
    import uuid
    return str(uuid.uuid1()).upper()



