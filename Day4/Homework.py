"""
1、位置参数个数不对，keyword参数传递名字不对时的报错信息查看（和上课原理保持一致即可）
2、多值参数练习，元组，字典的传参拆包练习（和上课原理保持一致即可）
3、练习列表传递到函数内，函数内取下标修改，函数外对应列表发生变化（和上课原理保持一致即可）
4、设计一个类，实例化1个对象，会实现下面两种行为（和上课保持一致即可）

需求
•一只 黄颜色 的 狗狗 叫 小黄
•具有  汪汪叫 行为
•具有  摇尾巴 行为
"""

'''
1、位置参数个数不对，keyword参数传递名字不对时的报错信息查看
'''
def print_info(name, age, gender):
    print(f'name:{name}')
    print(f'age:{age}')
    print(f'gender:{gender}')


# 位置参数传递个数不对
# print_info('小明', 21)

# keyword参数传递名字不对
# print_info(name='张三', age=35, sex='男')


'''
2、多值参数练习，元组，字典的传参拆包练习
'''
def mul_total(*args):
    """
    位置多值参数练习
    """
    total = 1
    for i in args:
        total *= i
    print(total)


# mul_total(1, 2, 3, 4, 5)


def print_info1(**kwargs):
    """
    keyword多值参数练习
    """
    print(kwargs)


# print_info1(namex='小明', age=20, sex='男')


def print_demo2(*args, **kwargs):
    """
    多值参数函数
    """
    print(args)
    print(kwargs)


def print_demo1(*args, **kwargs):
    """
    使用多值参数作为实参调用函数
    """
    print_demo2(args, kwargs)  # 变量名作为实参传的是对应的元组和字典
    print_demo2(*args, **kwargs)  # 加上*号对元组、字典进行拆包


# print_demo1(1, 2, 3, 4, 5, name='Alice', age=20, gender='女')


'''
3、练习列表传递到函数内，函数内取下标修改，函数外对应列表发生变化
'''
list1 = [32]


def change_list(list2):
    list2[0] = 40
    print(list2)


# change_list(list1)
# print(list1)


'''
4、设计一个类，实例化1个对象，会实现下面两种行为
需求
•一只 黄颜色 的 狗狗 叫 小黄
•具有  汪汪叫 行为
•具有  摇尾巴 行为
'''
class Animal:
    """
    动物类
    """

    # 定义初始化方法
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species

    # 定义打印方法
    def __str__(self):
        return f'{self.name}是一只{self.color}的{self.species}'

    # 定义汪汪叫方法
    def shout(self):
        print(f'{self.name}汪汪叫')

    # 定义摇尾巴方法
    def wag_tail(self):
        print(f'{self.name}摇尾巴')


# 实例化Animal的对象dog
dog = Animal('小黄', '黄颜色', '狗狗')

# 查看dog的信息
print(dog)

# 调用方法
dog.shout()
dog.wag_tail()
