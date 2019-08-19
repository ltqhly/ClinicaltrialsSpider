# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals
import json
import copy
import six

__all__ = ["BaseMixin", ]


class BaseMixin(object):
    config = None

    def auto_setup(self, config=None):
        if config is None:
            self.config = None
        elif isinstance(config, six.string_types):
            self.config = json.loads(config)
        elif isinstance(config, dict):
            self.config = copy.deepcopy(config)
        else:
            raise NotImplementedError
        if self.config is None:
            return

        for key, value in self.config.items():
            func = getattr(self, "_setup_{}".format(key), None) or getattr(self, "setup_{}".format(key), None)
            if func and callable(func):
                v = func(value)
                setattr(self, "_{}".format(key), v)
            # elif value and hasattr(self, key):
            #     setattr(self, key, value)

    def _setup_spider_config(self, config=None):
        return self._setup_spider(config=config)

    def _setup_spider(self, config=None):
        if not isinstance(config, dict):
            raise ValueError("ERROR spider:{}".format(config))
        self.spider_config = copy.deepcopy(config)
        return self.spider_config
