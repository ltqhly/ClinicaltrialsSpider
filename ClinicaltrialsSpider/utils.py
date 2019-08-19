# -*- coding: utf-8 -*-
# from __future__ import absolute_import, print_function, division, unicode_literals

import re
import logging
import json
import six
import traceback
from datetime import datetime, date, time, timedelta
from dateutil import parser
from nimbus_utils.timezone import make_aware, make_naive, is_aware, is_naive, now, utc
from nimbus_utils.encoding import smart_text, smart_bytes, smart_str
import time

# import datetime

INT = re.compile(r'\d')

__all__ = [
    "format_datetime",
    "trim_value",
    "get_num",
    "parse_datetime",
    "convert_to_int",
    "convert_dt2utc",
    "remove_r_n_t",
    "conver_str2datetime",
    "conver_toLocalTime",
    "format_datetime",
    "get_now",
]


def str_lower(value=None):
    '''
    转化小写
    :param value:
    :return:
    '''
    return value.lower()


def format_datetime(value=None, fmt="%Y-%m-%d %H:%M:%S"):
    '''
    dateime, time, date类型数据转化成format格式字符串
    :param value: value
    :param fmt: format
    :return:
    '''
    if isinstance(value, datetime):
        return value.strftime(fmt)
    elif isinstance(value, date):
        return value.strftime(fmt)
    elif isinstance(value, time):
        return value.strftime(fmt)
    elif isinstance(value, six.string_types):
        return parser.parse(value).strftime(fmt)
    return value


# print(format_datetime(value="2019-07-25T14:37:00Z", fmt="%Y-%m-%dT%H:%M:%SZ"))


def parse_datetime(value=None):
    try:
        if isinstance(value, datetime):
            return value
        elif isinstance(value, date):
            return value
        elif isinstance(value, time):
            return value
        elif isinstance(value, six.string_types):
            value = value.replace('[', '').replace(']', '')
        dt = parser.parse(value)
        return dt
    except Exception as e:
        traceback.print_exc()
        return datetime.now()


def convert_to_int(value=None, ):
    if not value:
        return 0
    if isinstance(value, six.string_types):
        value = "".join(INT.findall(value))
    try:
        value = int(value)
        return value
    except Exception as e:
        traceback.print_exc()
        return 0


def convert_to_utc(data=None, hours=8):
    dt = data - timedelta(hours=hours)
    return dt


def convert_dt2utc(data=None):
    if data and is_naive(data):
        data = make_aware(data, utc)
    elif data and is_aware(data):
        # starttime = make_aware(starttime, timezone.utc)
        data = data.astimezone(utc)
    return data


def trim_value(value, index=0, replaces=''):
    if isinstance(value, six.string_types):
        for replace in replaces:
            value = value.replace(replace, '')
        return value
    elif isinstance(value, (tuple, list)) and len(value) > index:
        return value[index]
    elif isinstance(value, (int, float)):
        return value
    else:
        return smart_str(value)


def get_num(value):
    num = re.findall("\d+", value)[0]
    return num


# def get_url_params(url):
#     urldata = url_parse.unquote(url)
#     result = url_parse.urlparse(urldata)
#     query_dict = url_parse.parse_qs(result.query)
#     return query_dict

def conver_str2datetime(value=None, fmt="%Y-%m-%dT%H:%M:%SZ"):
    '''
    字符串转化datetime类型
    :param value:
    :param fmt:
    :return:
    '''
    if isinstance(value, str):
        return datetime.strptime(value, fmt)
    return value


# def string_toTimestamp(value=None, fmt="%Y-%m-%dT%H:%M:%SZ"):
#     '''
#     :param value:  "2019-07-25T14:37:00Z"
#     :param fmt: "%Y-%m-%dT%H:%M:%SZ"
#     :return: 2019-07-25 22:37:00
#     '''
#     if isinstance(value, str):
#         utc_time = datetime.datetime.strptime(value, fmt)
#         local_time = utc_time + datetime.timedelta(hours=8)
#         local_time = format_datetime(local_time)
#         return isinstance(local_time, str)
#     return value


def conver_toLocalTime(data=None, hours=8):
    '''
    UTC时间转化为本地时间
    :param data: utc时间
    :param hours: 时差
    :return: datetime类型的本地时间
    '''
    dt = data + timedelta(hours=hours)
    return dt


def remove_r_n_t(value):
    '''
    去掉value中 \r \n \t
    :param value:
    :return: 如果为None, 无返回值
    '''
    if value:
        conver_value = value.replace("\n", "").replace("\r", "").replace("\t", "")
        if conver_value:
            return conver_value
        else:
            pass
    else:
        pass


def get_now(value):
    '''
    当前时间, create_time
    :param value:
    :return:
    '''
    now = datetime.now()
    return now


def remove_html(html):
    '''
    去掉html标签, 获取其中内容
    :param html:
    :return:
    '''
    reg = re.compile('<[^>]*>')
    text = reg.sub('', html)
    return text
