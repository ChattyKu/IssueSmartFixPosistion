import urllib.request
import json
import StrCommFunction
import copy

import time

check_url = 'http://whois.pconline.com.cn/ipJson.jsp?callback={}&ip={}'
flag = 'jsonFlagBegin'
all_data = dict()


def get_ip_detail_info(ip_add, data_manager):
    find_url = check_url.format(flag, ip_add)
    res_data = urllib.request.urlopen(find_url)
    res = res_data.read()
    res_str1 = res.decode("gb2312")
    dictinfo = json.loads(StrCommFunction.find_between_follow_flag(res_str1, 'jsonFlagBegin'))
    data_manager[ip_add] = copy.copy(dictinfo)


def get_all_info():
    file = open(r'E:\99_project\02_raspberrypi\aria2.log.20190705200051', encoding='utf-8')
    data = dict()
    for line in file:
        res = StrCommFunction.find_between_two_flag(line, 'Remote:', ',')
        if res != '':
            get_ip_detail_info(res[:res.find('(')], data)
    if data.__len__() == 0:
        pass

if __name__ == '__main__':
    get_all_info()