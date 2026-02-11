# 作者: 王道 龙哥
# 2026年02月10日11时14分36秒
# xxx@qq.com

def sum_total(*args):
    """
    args是一个元组
    :param args:
    :return:
    """
    total = 0
    for i in args:
        total += i
    print(total)


sum_total(1, 2, 3, 4, 5)
print('-' * 50)

print()


def print_demo2(*args, **kwargs):
    print(f'print_demo2 {args}')
    print(f'print_demo2 {kwargs}')


def print_demo(num, *args, **kwargs):
    """
    该函数处理了num参数
    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    print(num)
    # print(args)
    # print(kwargs)
    # kwargs {'name': 'Alice', 'age': 20, 'gender': '女'}
    # **kwargs  name="Alice", age=20, gender="女"
    print_demo2(*args, **kwargs)  # 元组拆包，字典拆包只会放到实参的位置


print_demo(1, 2, 3, 4, 5, name="Alice", age=20, gender="女")
