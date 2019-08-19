import requests
import sys
import time
import hashlib
import logging
import json
import random
import os
import sys

# -*- coding: UTF-8 –*-

proxy_username = 'lixp5788ap1'
proxy_passwd = '49014266'
proxy_server = '183.129.244.16'
proxy_port = '88'
pattern = 'json'
num = 1  # 获取端口数量
key_name = 'user_name='
key_timestamp = 'timestamp='
key_md5 = 'md5='
key_pattern = 'pattern='
key_num = 'number='
key_port = 'port='

a = os.path.realpath(__file__)
b = os.path.dirname(a)
PROXY_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'proxypool')
PROXY_FILE_NAME = "proxy_ip.json"
PROXY_FILE = os.path.join(PROXY_PATH, PROXY_FILE_NAME)

__all__ = [
    "get_new_proxy",
]


def _get_timestamp():
    timestamp = round(time.time() * 1000)
    return timestamp


def _get_md5_str(s):
    return hashlib.md5(bytes(s, encoding='utf8')).hexdigest()


def _get_open_url():
    time_stamp = _get_timestamp()
    md5_str = _get_md5_str(proxy_username + proxy_passwd + str(time_stamp))
    return 'http://' + proxy_server + ':' \
           + proxy_port + '/open?' + key_name + proxy_username + \
           '&' + key_timestamp + str(time_stamp) + \
           '&' + key_md5 + md5_str + \
           '&' + key_pattern + pattern + \
           '&' + key_num + str(num)


def _get_close_url(auth_port):
    time_stamp = _get_timestamp()
    md5_str = _get_md5_str(proxy_username + proxy_passwd + str(time_stamp))
    return 'http://' + proxy_server + ':' \
           + proxy_port + '/close?' + key_name + proxy_username + \
           '&' + key_timestamp + str(time_stamp) + \
           '&' + key_md5 + md5_str + \
           '&' + key_pattern + pattern + \
           '&' + key_port + auth_port


def _get_reset_url():
    time_stamp = _get_timestamp()
    md5_str = _get_md5_str(proxy_username + proxy_passwd + str(time_stamp))
    return 'http://' + proxy_server + ':' \
           + proxy_port + '/reset_ip?' + key_name + proxy_username + \
           '&' + key_timestamp + str(time_stamp) + \
           '&' + key_md5 + md5_str + \
           '&' + key_pattern + pattern


def testing(url, auth_port):
    proxies = {'http': "http://" + proxy_server + ':' + auth_port,
               'https': 'http://' + proxy_server + ':' + auth_port, }
    try:
        s = requests.Session()
        s.proxies.update(proxies)
        ret = s.get(url, timeout=5)
        msg = str(ret.status_code)

    except requests.exceptions.SSLError as e:
        msg = repr(e)

        # testing(url, auth_port)
    except Exception as e:
        msg = repr(e)

    return msg


def save_ip(json_obj):
    if not os.path.exists(PROXY_PATH):
        os.makedirs(PROXY_PATH)
    with open(PROXY_FILE, 'w') as result_file:
        json.dump(json_obj, result_file)
    result_file.close()


# def load_ip():
#     if not os.path.exists(PROXY_PATH):
#         os.makedirs(PROXY_PATH)
#     with open(PROXY_FILE, 'r') as result_file:
#         save_dict = json.load(result_file)
#         proxy = "https://" + save_dict["domain"] + ":" + str(random.choice(save_dict["port"]))
#         logging.info('load_ip||' + proxy)
#     result_file.close()
#     return proxy
#
#
# def remove_proxy():
#     os.remove(PROXY_FILE)


def get_new_proxy():
    proxy = ""
    try:
        open_url = _get_open_url()
        r = requests.get(open_url, timeout=3)
        result = str(r.content, encoding='utf8')
        # print(result)
        logging.info('open_url||' + repr(result))
        json_obj = json.loads(result)
        code = json_obj['code']
        if json_obj['code'] == 108:
            reset_url = _get_reset_url()
            r = requests.get(reset_url, timeout=3)
        elif json_obj['code'] == 100:
            proxy = "https://" + json_obj["domain"] + ":" + str(random.choice(json_obj["port"]))
            logging.info('get_new_proxy||' + repr(proxy))
        return proxy
    except Exception as e:
        logging.info('open_url||' + repr(e))
        return proxy

# proxy = get_new_proxy()
# print(proxy)
