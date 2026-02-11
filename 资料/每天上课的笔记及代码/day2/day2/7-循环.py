# 作者: 王道 龙哥
# 2026年02月08日16时36分50秒
# xxx@qq.com
import random

def use_while():
    i = 0
    while i < 5:
        print('HelloWorld')
        i += 1  # 循环体内必须有让判断趋近于假的操作，否则就会死循环


def sum_100():
    i = 1
    result = 0
    while i <= 100:
        result += i
        if result > 2000:
            break
        i += 1
    print(result, i)


def sum_even_100():
    i = 1
    result = 0
    while i <= 100:
        if i % 2 == 1:
            i += 1
            continue
        result += i
        i += 1
    print(result)


def daffodils():
    """
    求水仙花数
    :return:
    """
    num = 123
    while num <= 999:
        a = num % 10  # 个位
        b = num // 10 % 10
        c = num // 100
        if a ** 3 + b ** 3 + c ** 3 == num:
            print(num)
        num += 1
    # print(a)


def use_for():
    my_list = [1, 2, 3, 4, 5]  # 列表，是一种可迭代对象
    for i in my_list:
        print(i)
    print(i)  # 在for循环外，i的值是最后一个元素值


def use_for2():
    """
    遍历字符串
    :return:
    """
    for i in 'wangdao':
        print(i, end='  ')
    print()
    count = 0
    for i in '你好呀天气好':
        if i == '好':
            count += 1
    print(count)


def use_range():
    for i in range(1, 10, 2):
        print(i)


def print_star():
    i = 1
    while i <= 5:
        j = 1
        while j <= 8:
            print('*', end='')
            j += 1
        print()
        i += 1


def print_star2():
    i = 1
    while i <= 5:
        j = 1
        while j <= i:  # 内层控制多少列
            print('*', end='')
            j += 1
        print()
        i += 1


def use_while_else():
    num = 3
    my_list = [1, 2, 3, 4, 5]
    i = 0
    while i < 5:
        if my_list[i] == num:
            print('找到并显示你的成绩')
            break
        i += 1
    else:
        # 在循环体内没有break，就会走这里，有break，就不会走这里
        print('没找到你的成绩')


def use_for_else():
    num = 6
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        if num == i:
            print('找到并显示你的成绩')
            break
    else:
        # 在循环体内没有break，就会走这里，有break，就不会走这里
        print('没找到你的成绩')


def use_random():
    print(random.randint(1,5))

# use_while()
# sum_100()
# sum_even_100()
# daffodils()
# use_for()
# use_for2()
# use_range()
# print_star()
# print_star2()
# use_while_else()
# use_for_else()
use_random()