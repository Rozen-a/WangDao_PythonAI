# 作者: 王道 龙哥
# 2026年02月08日15时30分42秒
# xxx@qq.com

def use_cal():
    """
    算术运算符
    :return:
    """
    print(5 / 2)
    print(5 // 2)
    print(5 % 2)  # 取余
    print(5 ** 2)


def use_assign():
    num = 3
    num += 5
    print(num)


def use_compare():
    print(1 < 3)


def use_logic():
    print(5 and 3)  # 只需要掌握整体是 真，还是假即可
    print(0 or 5)
    print(not 0)


def use_bit():
    """
    位运算符
    :return:
    """
    print(5 & 7)
    print(5 | 7)
    print(~5)
    print(5 ^ 7)
    print(5 << 1)  # python左移永远都是乘2
    print(9 >> 1)  # 除2
    print(-9 >> 1)  # 先减1再除2
    print('-' * 50)
    print(5 ^ 5)  # 结果
    print(5 ^ 0)  # 结果


def find_one_number():
    """
    找出出现一次的那个数
    :return:
    """
    my_list = [5, 10, 8, 10, 5]
    result = 0
    for i in my_list:
        result ^= i
    print(result)


def use_ternary():
    """
    使用三目运算符
    :return:
    """
    a = 6
    b = 13
    max_num = a if a > b else b
    print(max_num)


def change_str():
    """
    类型转换
    :return:
    """
    score = 98.5
    name = '张三 '
    result = name + str(score)
    print(result)


# use_cal()
# use_assign()
# use_compare()
# use_logic()
# use_bit()
# find_one_number()
# use_ternary()
change_str()
