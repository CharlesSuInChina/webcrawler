# -*- coding:utf-8 -*-
import requests
import demo2

if __name__ == "__main__":
    url = "https://www.cau.edu.cn/"
    html = requests.get(url)
    # print html.content
    demo2.get_info_by_regular(html)
    print __file__
    print ""
    print "su hao"
#    get_info_by_regular()











