# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, division, unicode_literals
import scrapy
import requests
from scrapy.http import Request
import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http.response.html import HtmlResponse

from ClinicaltrialsSpider.items import ClinicaltrialsItem
from ClinicaltrialsSpider.loaders import ClinicaltrialsItemLoader
from ClinicaltrialsSpider.utils import remove_html
from .base import BaseSpider

class Clinicaltrials(BaseSpider):
    name = "clinicaltrials"

    def start_requests(self):
        data = {
            "draw": "2",
            "columns[0][data]": "0",
            "columns[0][name]": "",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "false",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "1",
            "columns[1][name]": "",
            "columns[1][searchable]": "false",
            "columns[1][orderable]": "false",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "2",
            "columns[2][name]": "",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "false",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "3",
            "columns[3][name]": "",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "false",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "4",
            "columns[4][name]": "",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "false",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "columns[5][data]": "5",
            "columns[5][name]": "",
            "columns[5][searchable]": "true",
            "columns[5][orderable]": "false",
            "columns[5][search][value]": "",
            "columns[5][search][regex]": "false",
            "columns[6][data]": "6",
            "columns[6][name]": "",
            "columns[6][searchable]": "true",
            "columns[6][orderable]": "false",
            "columns[6][search][value]": "",
            "columns[6][search][regex]": "false",
            "columns[7][data]": "7",
            "columns[7][name]": "",
            "columns[7][searchable]": "true",
            "columns[7][orderable]": "false",
            "columns[7][search][value]": "",
            "columns[7][search][regex]": "false",
            "columns[8][data]": "8",
            "columns[8][name]": "",
            "columns[8][searchable]": "true",
            "columns[8][orderable]": "false",
            "columns[8][search][value]": "",
            "columns[8][search][regex]": "false",
            "columns[9][data]": "9",
            "columns[9][name]": "",
            "columns[9][searchable]": "true",
            "columns[9][orderable]": "false",
            "columns[9][search][value]": "",
            "columns[9][search][regex]": "false",
            "columns[10][data]": "10",
            "columns[10][name]": "",
            "columns[10][searchable]": "true",
            "columns[10][orderable]": "false",
            "columns[10][search][value]": "",
            "columns[10][search][regex]": "false",
            "columns[11][data]": "11",
            "columns[11][name]": "",
            "columns[11][searchable]": "true",
            "columns[11][orderable]": "false",
            "columns[11][search][value]": "",
            "columns[11][search][regex]": "false",
            "columns[12][data]": "12",
            "columns[12][name]": "",
            "columns[12][searchable]": "true",
            "columns[12][orderable]": "false",
            "columns[12][search][value]": "",
            "columns[12][search][regex]": "false",
            "columns[13][data]": "13",
            "columns[13][name]": "",
            "columns[13][searchable]": "true",
            "columns[13][orderable]": "false",
            "columns[13][search][value]": "",
            "columns[13][search][regex]": "false",
            "columns[14][data]": "14",
            "columns[14][name]": "",
            "columns[14][searchable]": "true",
            "columns[14][orderable]": "false",
            "columns[14][search][value]": "",
            "columns[14][search][regex]": "false",
            "columns[15][data]": "15",
            "columns[15][name]": "",
            "columns[15][searchable]": "true",
            "columns[15][orderable]": "false",
            "columns[15][search][value]": "",
            "columns[15][search][regex]": "false",
            "columns[16][data]": "16",
            "columns[16][name]": "",
            "columns[16][searchable]": "true",
            "columns[16][orderable]": "false",
            "columns[16][search][value]": "",
            "columns[16][search][regex]": "false",
            "columns[17][data]": "17",
            "columns[17][name]": "",
            "columns[17][searchable]": "true",
            "columns[17][orderable]": "false",
            "columns[17][search][value]": "",
            "columns[17][search][regex]": "false",
            "columns[18][data]": "18",
            "columns[18][name]": "",
            "columns[18][searchable]": "true",
            "columns[18][orderable]": "false",
            "columns[18][search][value]": "",
            "columns[18][search][regex]": "false",
            "columns[19][data]": "19",
            "columns[19][name]": "",
            "columns[19][searchable]": "true",
            "columns[19][orderable]": "false",
            "columns[19][search][value]": "",
            "columns[19][search][regex]": "false",
            "columns[20][data]": "20",
            "columns[20][name]": "",
            "columns[20][searchable]": "true",
            "columns[20][orderable]": "false",
            "columns[20][search][value]": "",
            "columns[20][search][regex]": "false",
            "columns[21][data]": "21",
            "columns[21][name]": "",
            "columns[21][searchable]": "true",
            "columns[21][orderable]": "false",
            "columns[21][search][value]": "",
            "columns[21][search][regex]": "false",
            "columns[22][data]": "22",
            "columns[22][name]": "",
            "columns[22][searchable]": "true",
            "columns[22][orderable]": "false",
            "columns[22][search][value]": "",
            "columns[22][search][regex]": "false",
            "columns[23][data]": "23",
            "columns[23][name]": "",
            "columns[23][searchable]": "true",
            "columns[23][orderable]": "false",
            "columns[23][search][value]": "",
            "columns[23][search][regex]": "false",
            "columns[24][data]": "24",
            "columns[24][name]": "",
            "columns[24][searchable]": "true",
            "columns[24][orderable]": "false",
            "columns[24][search][value]": "",
            "columns[24][search][regex]": "false",
            "columns[25][data]": "25",
            "columns[25][name]": "",
            "columns[25][searchable]": "true",
            "columns[25][orderable]": "false",
            "columns[25][search][value]": "",
            "columns[25][search][regex]": "false",
            "start": "0",
            "length": "29701",
            "search[value]": "",
            "search[regex]": "false"
        }

        # url = 'https://clinicaltrials.gov/ct2/results/rpc/Yi0n'
        url = 'https://clinicaltrials.gov/ct2/search/browse?brwse=cond_alpha_all'
        req = scrapy.FormRequest(url, formdata=data, callback=self.parse)
        yield req

    def parse(self, response):
        body = response.body
        msg_list = body.decode(encoding='utf-8')
        data_str = re.findall(r'<script type="text/javascript">\nvar tableData1 =([\s\S]+?)];.*?', msg_list)[0]
        data_str = data_str.replace('\n', '').replace('\t', '').replace('\r', '').replace(' [        ', '').replace('\\', '')
        rule_text = r'>.*?</a>.*?]'
        data_list = re.findall(rule_text, data_str, re.I | re.S | re.M)
        for data in data_list:
            conditions_rule = r'>.*?</a>'
            keyword = re.findall(conditions_rule, data, re.I | re.S | re.M)
            conditions = keyword[0].replace('>', "").replace('</a', "")
            url = 'https://clinicaltrials.gov/ct2/results?cond="{}"'.format(conditions)
            studies_rule = r'" .*?"'
            studies = re.findall(studies_rule, data, re.I | re.S | re.M)[0].replace('" ', '').replace('"', '')
            meta = {"conditions": conditions, "studies": studies}
            yield Request(url, callback=self.detail, meta=meta)

    def detail(self, response):
        conditions = response.meta.get("conditions", "")
        studies = response.meta.get("studies", "")
        body = requests.get(response.url)
        html_response = HtmlResponse(url=response.url, body=body.text, encoding="utf-8")
        tr_list = response.xpath('//table[@id="theDataTable"]/tbody/tr').extract()
        for tr in tr_list:
            tr = tr.replace('\r', '').replace('\n', '').replace('\t', '')
            data_rule = r'<td>.*?</td>'
            data_list = re.findall(data_rule, tr, re.I | re.S | re.M)
            all_data = []
            for data in data_list:
                data = remove_html(data)
                all_data.append(data)
            l = ClinicaltrialsItemLoader(item=ClinicaltrialsItem(), response=html_response)
            l.add_value("conditions", conditions)
            l.add_value("studies", studies)
            l.add_value("row", all_data[0])
            l.add_value("nct_number", all_data[1])
            l.add_value("status", all_data[2])
            l.add_value("study_title", all_data[3])
            l.add_value("detail_conditions", all_data[4])
            l.add_value("interventions", all_data[5])
            l.add_value("study_type", all_data[6])
            l.add_value("phase", all_data[7])
            l.add_value("sponsor_collaborators", all_data[8])
            l.add_value("funder_type", all_data[9])
            l.add_value("study_design", all_data[10])
            l.add_value("outcome_measures", all_data[11])
            l.add_value("number_enrolled", all_data[12])
            l.add_value("sex", all_data[13])
            l.add_value("age", all_data[14])
            l.add_value("other_ids", all_data[15])
            l.add_value("title_acronym", all_data[16])
            l.add_value("study_start", all_data[17])
            l.add_value("primary_completion", all_data[18])
            l.add_value("study_completion", all_data[19])
            l.add_value("first_posted", all_data[20])
            l.add_value("last_update_posted", all_data[21])
            l.add_value("results_first_posted", all_data[22])
            l.add_value("locations", all_data[23])
            l.add_value("study_documents", all_data[24])
            item = l.load_item()
            yield item
