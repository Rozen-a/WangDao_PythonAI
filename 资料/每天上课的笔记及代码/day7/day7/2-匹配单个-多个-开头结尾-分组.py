# 作者: 王道 龙哥
# 2026年02月13日10时45分38秒
# xxx@qq.com
import re


def match_single():
    pattern = r"[a-zA-Z]\d[a-zA-Z]"
    texts = ["a1b", "B2C", "x3y", "1ab"]
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(ret.group())
        else:
            print(f'{text}没有匹配')


def match_more1():
    pattern = r"\d+"  # 1次或多次数字
    texts = ["20", "3", "abc", "123"]
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(ret.group())
        else:
            print(f'{text}没有匹配')


def match_more2():
    pattern = r"[a-zA-Z]{3,6}"
    texts = ["abc", "abcd12", "ab", "abcdef"]
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(ret.group())
        else:
            print(f'{text}没有匹配')


def match_start_end():
    pattern = r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$"
    emails = ["user@163.com", "user@.com", "abc@123", "user@163.com.abc"]
    for text in emails:
        ret = re.match(pattern, text)
        if ret:
            print(ret.group())
        else:
            print(f'{text}没有匹配')


def match_group():
    pattern = r"(\w+)@(\w+\.\w+)"  # 分组1：用户名，分组2：域名
    email = "user123@example.com"
    ret = re.match(pattern, email)
    if ret:
        print(ret.group(1))
        print(ret.group(2))
        print(ret.group())


def match_group2():
    texts = ["09", "9", "0", "99", '100']
    # ^ (100|[1-9]?\d)$

    pattern = r'0$|100|[1-9]\d?'
    for text in texts:
        ret = re.match(pattern, text)
        if ret:
            print(ret.group())
        else:
            print(f'{text}没有匹配')


def match_group3():
    pattern = r'^(\w+)\s+\1$'

    tests = [
        "hello hello",
        "test test",
        "hello world"
    ]

    for t in tests:
        print(t, bool(re.match(pattern, t)))


if __name__ == '__main__':
    # match_single()
    # match_more1()
    # match_more2()
    # match_start_end()
    # match_group()
    # match_group2()
    match_group3()
