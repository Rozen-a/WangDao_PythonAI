# 作者: 王道 龙哥
# 2026年02月10日10时31分46秒
# xxx@qq.com
# 定义加法函数
def get_sum(a, b):
    return a + b


# 定义减法函数
def get_substract(a, b):
    return a - b


# a = get_sum
# print(a(1, 2))

# 定义计算函数
def calculate(a, b, fn):
    """
    自定义函数, 模拟计算器, 传入什么 函数(对象), 就做什么操作.
    :param a: 要操作的第1个整数
    :param b: 要操作的第2个整数
    :param fn: 具体的操作规则
    :return: 计算结果.
    """
    return fn(a, b)

#传递行为
print(calculate(10, 20, get_sum))
print(calculate(10, 20, get_substract))
