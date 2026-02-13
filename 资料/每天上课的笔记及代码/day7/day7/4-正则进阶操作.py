# 作者: 王道 龙哥
# 2026年02月13日14时31分52秒
# xxx@qq.com
import re


def use_compile():
    pattern = re.compile(r"1[34578]\d{9}")

    # 多次使用预编译的Pattern对象
    texts = ["文本1：13812345678", "文本2：13987654321", "文本3：abc123"]
    for text in texts:
        result = pattern.search(text)  # 直接用Pattern对象调用search
        if result:
            print(f"{text}-------提取到手机号：{result.group()}")
        else:
            print(f"{text}-------未提取到")


def use_flags():
    pattern = r"hello"
    text = "Hello HELLO hello"

    # 不忽略大小写：只匹配小写hello
    print(re.findall(pattern, text))

    print(re.findall(pattern, text, re.I))


def find_second_match(pattern, text):
    # finditer返回一个迭代器
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


def use_find_second_match():
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)


# 我们要实现一个和range类似的生成器
def my_range(n):
    i = 0
    while i < n:
        yield i  # 冻结当前执行位置，并返回i
        i += 1
    return None


def use_generator():
    """
    使用生成器
    :return:
    """
    # 生成器
    g = my_range(10)
    print(g)
    # result=next(g)
    # print(result)
    # result=next(g)
    # print(result)
    for i in my_range(10):
        print(i)


from collections.abc import Iterable, Iterator


def use_for():
    my_list = [1, 2, 3]  # 可迭代对象
    print(isinstance(my_list, Iterable))  # 判断是否是可迭代对象
    list_iterator = iter(my_list)
    print(isinstance(list_iterator, Iterator))  # 判断是否是迭代器
    for i in list_iterator:
        print(i)
    for i in list_iterator:
        print(i)


if __name__ == '__main__':
    # use_compile()
    # use_flags()
    # use_find_second_match()
    # use_generator()
    use_for()
