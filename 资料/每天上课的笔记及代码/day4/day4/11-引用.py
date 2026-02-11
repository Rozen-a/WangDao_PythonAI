# 作者: 王道 龙哥
# 2026年02月10日14时25分58秒
# xxx@qq.com

def use_int():
    """
    理解整型变量，引用设计
    :return:
    """
    a = 1
    print(id(a))  # id可以看到对象的地址

    b = a
    print(id(b))

    a = 5
    print(f'a变为5后{id(a)}')
    print(id(b))
    print(b)



use_int()

num = 10


def change(num1):
    """
    （不考虑全局变量）不可变类型，无法在函数内修改函数外某个变量的值
    :param num1:
    :return:
    """
    num1 = 5


print(f'change之前{num}')
change(num)
print(f'change之后{num}')
print('-' * 50)

num_list = [10]
num_list1 = num_list
print(id(num_list))
print(id(num_list1))
num_list[0]=5
print(num_list1)

print(f'修改某个元素后{id(num_list)}')
print(f'修改某个元素后{id(num_list1)}')

