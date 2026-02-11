# 作者: 王道 龙哥
# 2026年02月09日14时28分50秒
# xxx@qq.com


t1 = (10,)
print(type(t1))
for i in t1:
    print(i)


# 1. 定义一个元组
tup = ('aa','bb','cc','dd','ee', 'bb', 'cc')

# 2. 查找某个元素 index()
print(tup.index('bb'))                              # 1
print(tup.index('bb',3,6))      # 5

# 3. 统计某个元素出现的次数 count()
print(tup.count('aa'))                              # 1
print(tup.count('bb'))                              # 2

# 4. 统计元组中元素的总个数 len()
print(len(tup))                                     # 7

# 5. 根据下标获取元素的值
print(tup[3])


name_list = list(tup)								# 把元组转为列表
print(name_list)
tup2 = tuple(name_list)						      # 把列表转为元组
print(tup2)

str1='hello'
list1=list(str1)
print(list1)
print(''.join(list1))