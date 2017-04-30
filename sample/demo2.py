# -*- coding:utf-8 -*-

from lxml import etree
import re

def get_info_by_regular(html):
    urls = re.findall("<a href=\"(.*?)\">", html.content, re.S)
    print ""
    for each in urls:
        print each
        # urlsStr = ""
        # for each in urls:
        #     urlsStr = urlsStr + each + "\r\n"
        # print urlsStr

def get_info_by_xpath():
    selector = etree.HTML(html.content)
    selector.XPath()