# 作者: 王道 龙哥
# 2026年02月09日15时53分37秒
# xxx@qq.com

my_set = {10, 20, 30, 40}
print(my_set)
my_set.add(50)
print(my_set)

# 3. 通过别的序列来创建集合
myset1 = set("wangdao")					# 通过字符串创建集合
myset2 = set([10,20,30,40,10,20])		# 通过列表创建集合
myset3 = set((10,20,30,40,10,20))		# 通过元组创建集合

print(10 in my_set)
print(10 not in my_set)

my_set = {'a','b',1,2}
my_set.add('张飞')        			# {1, 2, 'a', 'b', '张飞'}
my_set.add('a')          			 # {1, 2, '张飞', 'a', 'b'}

my_set.update('李四')     			# {'b', 2, 1, '四', '李', '张飞', 'a'}
my_set.update('A')       			 # {1, 2, 'A', 'b', '张飞', '李', '四', 'a'}
my_set.update(["李云龙","楚云飞"])   	 # {'a', 1, 2, '楚云飞', 'b', '李', '四', '张飞', 'A', '李云龙'}


# 添加元素
my_set.update(["李云龙","楚云飞"])   	 # {'a', 1, 2, '楚云飞', 'b', '李', '四', '张飞', 'A', '李云龙'}
print(my_set)
# 3. 删除元素
my_set.remove('A')      			 # {1, 2, '李', 'b', '李云龙', 'a', '四', '楚云飞', '张飞'}
# my_set.remove("丁伟")  			    # 丁伟不存在于集合，会报错
print(my_set)
my_set.discard('李云龙')   		   # {1, 2, '四', '张飞', '李', 'a', '楚云飞', 'b'}
my_set.discard("丁伟")  				# 丁伟不存在于集合，不会报错
print(my_set)

print('-'*50)
# 4. 求交集、并集和差集
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# 并集
union_set = set1 | set2
print(union_set)					# 输出: {1, 2, 3, 4, 5, 6}

# 差集
diff_set = set1 - set2
print(diff_set)						# 输出: {1, 2}

# 交集
inter_set = set1 & set2
print(inter_set)