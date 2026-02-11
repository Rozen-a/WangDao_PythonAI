# 作者: 王道 龙哥
# 2026年02月10日15时23分34秒
# xxx@qq.com

my_list = [1, 2, 3]
my_list1 = my_list.copy()
print(id(my_list))
print(id(my_list1))
my_list[0] = 10
print(my_list, my_list1)

print('-' * 50)


def get_sum(a, b):
    return a + b


def cal_num(a, b, fn):
    print(fn(a, b))


cal_num(10, 20, get_sum)
# 匿名函数可以提高阅读效率，只会在某个地方使用一次
cal_num(10, 20, lambda a, b: a + b)


#不太理解，到11章再学习
str_list = ['a', 'B', 'c', 'bc']

print(sorted(str_list, key=lambda x: x.lower()))
