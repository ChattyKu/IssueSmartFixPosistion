import os
SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
START_SYMBOLS = ['{', '[', '(', '<']
# 存储左括号和右括号
open_brackets = '([{<'
close_brackets = ')]}>'


def find_between_follow_flag(des_str, flag_str):
    """
    获取字符串中否个标志位后的区域分割符号开始与它匹配的区域结束符号之间的字符串
    EXP:
        dex_str = abc abc(abcdefghi)
        flag_str = abc
        返回 abcdefghi
    :param des_str: 源字符串
    :param flag_str: 需要解析的分割为标志前置标志
    :return: 匹配的两个区域标志之间的字符串
    """
    res = ''
    begin = 0
    while True:
        index_key_point = des_str.find(flag_str, begin)
        key_flag = dict()
        if index_key_point == -1:
            print("not find flag, please check param 2")
            return res
        else:
            if des_str[index_key_point + flag_str.__len__()] in START_SYMBOLS:
                key_flag['i'] = index_key_point + flag_str.__len__() + 1
                key_flag['f'] = des_str[index_key_point + flag_str.__len__()]
                break
            else:
                begin = index_key_point + flag_str.__len__()
    stack = []
    for index in range(des_str.__len__()):
        if des_str[index] in open_brackets:  # 区域开始
            if index == key_flag['i']:
                key_flag['begin_in_stack'] = stack.__len__()
            stack.append(des_str[index])
        elif des_str[index] in close_brackets:  # 区域结束
            stack.pop()
            if 'begin_in_stack' in key_flag and stack.__len__() == key_flag['begin_in_stack']:
                return des_str[key_flag['i']:index + 1]
        else:
            continue
    return res


def find_between_two_flag(des_str, flag_beg, flag_end):
    beg_index = des_str.find(flag_beg)
    res = ''
    if beg_index == -1:
        print("not find begin flag")  # debug
        return res
    end_index = des_str.find(flag_end, beg_index + flag_beg.__len__())
    if end_index == -1:
        print("not find end flag")
        return res
    if end_index < beg_index:
        return res
    return des_str[beg_index + flag_beg.__len__():end_index]


def get_path_and_name(path):
    """
    根据路径名称获得文件名称和路径
    :param path: 全路径
    :return: 路径，文件名
    """
    return os.path.dirname(path), os.path.basename(path)


if __name__ == '__main__':
    des = """
    




if(window.jsonFlagBegin) {jsonFlagBegin({"ip":"202.101.172.35","pro":"浙江省","proCode":"330000","city":"杭州市",
"cityCode":"330100","region":"","regionCode":"0","addr":"浙江省杭州市 电信","regionNames":"","err":""});}



"""
    flag = 'jsonFlagBegin'
    res = find_between_follow_flag(des, flag)

    des = '2019-07-06 13:17:46.686101 [INFO] [DHTMessageDispatcherImpl.cc:79] Message sent: ' \
          'dht query find_node TransactionID=8773788e Remote:195.154.181.225(51272), ' \
          'id=a026363823a6275c34841d5230b1f7a23eb80fe3, v=A2%00%03, target'
    b_f = 'Remote:'
    e_f = ','
    res = find_between_two_flag(des, b_f, e_f)

    print(res)
