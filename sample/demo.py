# -*- coding:utf-8 -*-
import requests
import re
from lxml import etree
url = "https://www.cau.edu.cn/"
html = requests.get(url)
print html.content

# urls = re.findall("<a href=\"(.*?)\">", html.content, re.S)
# urlsStr = ""
# for each in urls:
#     urlsStr = urlsStr + each + "\r\n"
# print urlsStr

selector = etree.HTML(html.content)
selector.XPath()






