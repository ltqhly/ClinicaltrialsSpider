# -*- coding: utf-8 -*-
# import sys

# sys.setdefaultencoding('utf-8')

import json

import requests
from scrapy import cmdline

# cmdline.execute("scrapy crawl wechat".split())

# cmdline.execute("scrapy crawl weibo".split())
#
# urll = 'http://dynamic.goubanjia.com/dynamic/get/69a96f494e974911b14e3b177fc3dac9.html'
# r = requests.get(url=urll)
# ipp = r.content.replace('\n', '')

config = {
    "spider_config": {
        # "keywords": [
        #     # 'WuXi',
        #     'ShangHai',
        #     # 'Beijing',
        # ]
    }
}
config_json = json.dumps(config)
config_spider = "clinicaltrials"

cmd = u"""scrapy||crawl||-a||config={config}||{spider}""".format(config=config_json, spider=config_spider)

cmds = cmd.split("||")
print (cmds)

# cmdline.execute('scrapy crawl dxy -a para=pata'.split())
cmdline.execute(cmds)

# time   去重  word datedelta redis里加url去重    url（SpiderID+URL(MD5)）proxy


# sname(ok)    all表(ok)   时间字段   content变成tuple（ok）   时区(UTC)   dxy去重（在redis中）


# wechat dxy去重  ， dxy点赞
