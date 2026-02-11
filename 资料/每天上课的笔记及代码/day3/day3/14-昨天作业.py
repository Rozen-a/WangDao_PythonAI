# 作者: 王道 龙哥
# 2026年02月09日16时59分35秒
# xxx@qq.com

def homework4():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j}*{i}={i * j}', end='\t')
        print()


def homework4_2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j}*{i}={i * j:<2d}', end='  ')  # 小于号是左对齐
        print()


def homework5():
    """
    输出该整数的二进制包含1的个数
    :return:
    """
    while True:  # 为了高效测试
        num = int(input('输入一个数'))
        flag = 1
        count = 0  # 统计1的个数
        for i in range(64):
            if flag & num:
                count += 1
            flag <<= 1
        print(count)


# homework4()
# homework4_2()
homework5()
