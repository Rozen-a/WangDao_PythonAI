def test1():
    """
    1.自己定义变量赋值不同的数据类型并打印，并使用type（与上课一致）
    """
    # 整型
    data1 = 456
    print(data1)
    type_data1 = type(data1)
    print(type_data1)

    # 浮点型
    data2 = 5.6
    print(data2)
    type_data2 = type(data2)
    print(type_data2)

    # 布尔型
    data3 = False
    print(data3)
    type_data3 = type(data3)
    print(type_data3)

    # 字符串类型
    data4 = "wangdao"
    print(data4)
    type_data4 = type(data4)
    print(type_data4)


def test2():
    """
    2.使用input读取数据并转为整数（与上课一致）
    """
    print("输入一个数字：", end = '')
    data = input()
    data_int = int(data)
    print(f'该数加5得：{5 + data_int}')


def test3():
    """
    3.实现从1到100之间的奇数求和
    """
    i = 1
    num = 0
    while i <= 100:
        num += i
        i += 2
    print(f'从1到100之间的奇数和是{num}')


def test4():
    """
    4.
    打印九九乘法表（直接百度乘法表图像，与其一致即可，和课件的一致也可以）
    """
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print(f'{j}*{i}={i*j}',end = '\t')
            j += 1
        print()
        i += 1

def test5():
    """
    难度作业：
    5.
    统计一个整数对应的二进制数的1的个数。输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数
    """
    num = int(input())
    if num < 0:
        num += 1<<64 # 转换为补码对应的无符号整数
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num >>= 1
    print(count)

# test1()
# test2()
# test3()
# test4()
test5()
