# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals
from datetime import datetime, timedelta, date
from dateutil import parser
from scrapy.loader.processors import Join, MapCompose, TakeFirst, Identity
from w3lib.html import remove_tags
from scrapy.loader import ItemLoader
from ..utils import *

from ClinicaltrialsSpider.items import ClinicaltrialsItem


class ClinicaltrialsItemLoader(ItemLoader):
    default_item_class = ClinicaltrialsItem
    default_input_processor = MapCompose(remove_tags)
    default_output_processor = TakeFirst()
    create_time_in = MapCompose(format_datetime, )

