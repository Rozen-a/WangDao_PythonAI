# 作者: 王道 龙哥
# 2026年02月13日15时31分29秒
# xxx@qq.com
import re


def use_greedy_pattern():
    text = "<div>内容1</div><div>内容2</div>"

    # 1. 贪婪匹配（.*尽可能多匹配，从第一个<div>到最后一个</div>）
    greedy_pattern = r"<div>.*</div>"

    result = re.findall(greedy_pattern, text)
    print(result)


def use_non_greedy_pattern():
    text = "<div>内容1</div><div>内容2</div>"

    # 1. 贪婪匹配（.*尽可能多匹配，从第一个<div>到最后一个</div>）
    greedy_pattern = r"<div>.*?</div>"

    result = re.findall(greedy_pattern, text)
    print(result)


def use_r():
    pattern = r'C\\'  # 代表原生子串，直接加r
    ret = re.match(pattern, 'C\\')
    if ret:
        print(ret.group())


if __name__ == '__main__':
    # use_greedy_pattern()
    # use_non_greedy_pattern()
    use_r()
