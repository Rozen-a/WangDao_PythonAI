# 作者: 王道 龙哥
# 2026年02月13日10时29分58秒
# xxx@qq.com
import re


def match1():
    # 2. 匹配
    original_data = 'wangdao@cskaoyan.com'

    result = re.match('wangdao', original_data)
    if result:
        print(result.group())


def match2():
    # ^1: 表示以1开头
    # [34578]: 第二位是3,4,5,7,8其中的一个
    # \d: 匹配任意数字
    # {9}: 任意数字出现9次
    # $: 结束符，表示到此结束
    pattern = r"^1[34578]\d{9}$"
    text1 = "13812345678"  # 合法手机号
    text2 = "12345678901"  # 非法手机号（开头不符）
    result = re.match(pattern, text1)
    if result:
        print(result.group())
    else:
        print(f'{text1}没有匹配')
    result = re.match(pattern, text2)
    if result:
        print(result.group())
    else:
        print(f'{text2}没有匹配')


if __name__ == '__main__':
    # match1()
    match2()
