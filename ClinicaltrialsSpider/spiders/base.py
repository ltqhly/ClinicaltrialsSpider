# -*- coding: utf-8 -*-
import traceback
import logging
from scrapy.spiders import Spider
from .BaseMixin import BaseMixin
import copy
import json

class BaseSpider(BaseMixin, Spider):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        cls.spider_kwargs = copy.deepcopy(kwargs)
        config = kwargs.pop("config", None)
        spider = super(BaseSpider, cls).from_crawler(crawler, *args, **kwargs)
        try:
            spider.log(message="spider_name: {}".format(spider.name), level=logging.INFO)
            spider.log(message="spider_kwargs: {}".format(spider.spider_kwargs), level=logging.INFO)
            if config is None:
                spider.log(message="config is None", level=logging.ERROR)
            else:
                spider.log(message=config, level=logging.DEBUG)
                spider.auto_setup(config)
                spider.log(
                    "CONFIG config: {config}".format(config=json.dumps(spider.config, ensure_ascii=False, indent=2)),
                    level=logging.INFO)
                spider.log("SPIDER spider_config: {config}".format(
                    config=json.dumps(spider.spider_config, ensure_ascii=False, indent=2)), level=logging.INFO)
        except ValueError as e:
            spider.log(e, level=logging.ERROR)
            raise e
        except Exception as e:
            spider.log(e, level=logging.ERROR)
            traceback.print_exc()
        return spider
