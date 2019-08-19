# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time
import random
import logging
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from ..utils_proxy import get_new_proxy


class NewtworkRetryMiddleware(RetryMiddleware):
    logger = logging.getLogger(__name__)

    # def delete_proxy(self, proxy):
    #     if proxy:
    #         # delete proxy from proxies pool
    #         remove_proxy()

    # get_new_proxy()

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            # 删除该代理
            older_proxy = request.meta.get('proxy', False)
            if older_proxy and older_proxy == spider.config["spider_config"].get("proxy"):
                proxy = get_new_proxy()
                request.meta['proxy'] = proxy
                spider.config["spider_config"]["proxy"] = proxy
                # time.sleep(random.randint(3, 5))
            self.logger.warning('返回值异常, 进行重试...')
            return self._retry(request, reason, spider) or response
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            # 删除该代理
            older_proxy = request.meta.get('proxy', False)
            if older_proxy and older_proxy == spider.config["spider_config"].get("proxy"):
                spider.config["spider_config"].pop("proxy")
                proxy = get_new_proxy()
                request.meta['proxy'] = proxy
                spider.config["spider_config"]["proxy"] = proxy
                # time.sleep(random.randint(3, 5))
            self.logger.warning('连接异常, 进行重试...')
            return self._retry(request, exception, spider)
