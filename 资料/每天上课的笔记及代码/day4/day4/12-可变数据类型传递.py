# 作者: 王道 龙哥
# 2026年02月10日14时54分18秒
# xxx@qq.com
num_list = [10]


def change_list(num_list1):
    """
    在函数内要使用对应的方法来操作 可变类型
    :param num_list1:
    :return:
    """
    num_list1[0] = 5
    num_list1.append(15)

print(f'change之前{num_list}')
change_list(num_list)
print(f'change之后{num_list}')
