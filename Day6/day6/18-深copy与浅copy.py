# 作者: 王道 龙哥
# 2026年02月12日17时07分00秒
# xxx@qq.com
import copy


class Student:
    def __init__(self, name):
        self.name = name


def use_copy():
    s1 = Student('张三')
    s2 = copy.copy(s1)  # 浅copy

    s2.name = '李四'
    print(s1.name)


def use_deepcopy():
    a = [1, 2]
    b = [10, 20]
    c = [a, b]
    # d=c.copy() #浅copy
    d = copy.deepcopy(c)
    print(c is d)
    print(id(c))
    print(id(d))
    print('-' * 60)
    print(id(c[0]))
    print(id(d[0]))
    a[0] = 5
    print(c)
    print(d)


if __name__ == '__main__':
    # use_copy()
    use_deepcopy()
