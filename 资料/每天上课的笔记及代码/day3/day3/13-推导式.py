# 作者: 王道 龙哥
# 2026年02月09日16时47分58秒
# xxx@qq.com

num_list = [i for i in range(10)]

print(num_list)

# 只需要偶数
num_list = [i for i in range(10) if i % 2 == 0]

print(num_list)

# if else

num_list = [i if i % 2 == 0 else i ** 2 for i in range(10)]

print(num_list)

print('-' * 50)
# 字典生成式
word_list = ['hello', 'today', 'good', 'day']
word_dict = {v: k for k, v in enumerate(word_list)}
print(word_dict)

# 集合生成式（推导式） 不重要
numbers = [1, 2, 2, 3, 4, 4]
set2={num*num for num in numbers}
print(set2)