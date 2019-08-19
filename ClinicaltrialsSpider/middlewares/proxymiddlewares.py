# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from ..utils_proxy import get_new_proxy
from scrapy.downloadermiddlewares import httpproxy


class HttpbinProxyMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        proxy = spider.config["spider_config"].get("proxy", False)
        if not proxy:
            proxy = get_new_proxy()
            # proxiess = load_ip()

        spider.config["spider_config"]["proxy"] = proxy
        request.meta['proxy'] = proxy
        # spider.config["spider_config"]["proxy"] = proxy
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        proxy = get_new_proxy()
        request.meta['proxy'] = proxy
        spider.config["spider_config"]["proxy"] = proxy
        # print(request.meta['proxy'])
        # spider.config["spider_config"]["proxy"] = "sdafsdaf"
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
        # proxy = get_new_proxy()
        # spider.config["spider_config"]["proxy"] = proxy
