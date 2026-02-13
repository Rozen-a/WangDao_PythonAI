# 作者: 王道 龙哥
# 2026年02月12日16时53分12秒
# xxx@qq.com

import sys


def use_argv():
    print(sys.argv)


def read_conf():
    with open('my_conf', 'r', encoding='utf8') as f:
        my_dict=eval(f.read())
        print(type(my_dict))
        print(my_dict)


# use_argv()
read_conf()