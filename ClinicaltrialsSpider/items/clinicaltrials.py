# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals
import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, TakeFirst, Identity
from scrapy.loader.processors import Compose, SelectJmes, MergeDict
from scrapy.loader import ItemLoader
from scrapy.item import Item
from .base import BaseItem


class ClinicaltrialsItem(BaseItem):
    conditions = scrapy.Field()
    studies = scrapy.Field()
    row = scrapy.Field()
    nct_number = scrapy.Field()
    status = scrapy.Field()
    study_title = scrapy.Field()
    detail_conditions = scrapy.Field()
    interventions = scrapy.Field()
    study_type = scrapy.Field()
    phase = scrapy.Field()
    sponsor_collaborators = scrapy.Field()
    funder_type = scrapy.Field()
    study_design = scrapy.Field()
    outcome_measures = scrapy.Field()
    number_enrolled = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    other_ids = scrapy.Field()
    title_acronym = scrapy.Field()
    study_start = scrapy.Field()
    primary_completion = scrapy.Field()
    study_completion = scrapy.Field()
    first_posted = scrapy.Field()
    last_update_posted = scrapy.Field()
    results_first_posted = scrapy.Field()
    locations = scrapy.Field()
    study_documents = scrapy.Field()
