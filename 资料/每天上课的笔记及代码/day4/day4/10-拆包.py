# 作者: 王道 龙哥
# 2026年02月10日14时14分22秒
# xxx@qq.com
# 对列表拆包
my_list = [1, 3.14, 'Cskaoyan', True]
num, pi, name, my_bool = my_list
print(f"num:{num}, pi:{pi}, name:{name}, my_bool:{my_bool}")

# 对字典拆包
dict1 = {'name': '李云龙', 'age': 20, 'gender': '男'}

# 对字典拆包的时候，获取到的是key值
key1, key2, key3 = dict1
print(f"key1:{key1},key2:{key2},key3:{key3}")

a, b = 10, 20

a, b = b, a  #交换两个值
print(a, b)
