"""
1、完成列表、字典的增删查改（代码与上课保持一致）

完成字符串的切片:
num_str = "0123456789"
截取从 2 ~ 5 位置 的字符串
截取从 2 ~ 末尾的字符串
截取从 开始~ 5 位置 的字符串
截取完整的字符串
从开始位置，每隔一个字符截取字符串
从索引 1 开始，每隔一个取一个
截取从 2 ~ 末尾 - 1的字符串
截取字符串末尾两个字符
字符串的逆序（面试题）

使用enumerate把seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 变为一个字典，效果和上课一致
"""

'''
列表增删查改
'''
def list_add():
    """
    列表添加
    :return:
    """
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.append('luoxiye')
    print(name_list)
    city_list = ['北京', '上海', '广州', '深圳']
    new_city_list = ['成都', '杭州', '重庆', '武汉']

    # 扩展
    city_list.extend(new_city_list)
    print(city_list)

    # 插入
    name_list.insert(1, 'Bob')
    print(name_list)


def list_search():
    """
    列表查询
    :return:
    """
    my_list = ['小李', '小明', '嘉豪', '小张', '嘉豪', '老王', '老李', '楚云飞', '嘉豪']

    # 查找匹配项
    print(my_list.index('嘉豪'))
    print(my_list.index('嘉豪', 3))
    print(my_list.index('嘉豪', 3, 10))

    # 统计出现次数
    print(my_list.count('嘉豪'))
    print(my_list.count('风华'))

    # 判断存在
    print('小李' in my_list)

    # 判断不存在
    print('小李' not in my_list)


def list_del():
    """
    列表删除
    :return:
    """
    # 删除指定位置元素
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    del hero_list[1]
    print(hero_list)

    # 删除指定位置元素并返回值
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    print(hero_list.pop()) # 默认删除最后一个
    print(hero_list)
    print(hero_list.pop(0)) # 删除第一个
    print(hero_list)

    # 删除第一个等于指定值元素
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖', '宋江']
    hero_list.remove('宋江')
    print(hero_list)

    # 删除所有等于指定值的元素
    hero_list = ['吴用', '宋江', '宋江', '鲁智深', '林冲', '花荣', '晁盖', '宋江']
    i = 0
    while i < len(hero_list):
        if hero_list[i] == '宋江':
            del hero_list[i] # 删除元素时不移动指针
        else:
            i += 1
    print(hero_list)


def list_modify():
    """
    列表修改
    :return:
    """
    # 修改
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    hero_list[0] = '智多星'
    print(hero_list)

    # 反转
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    hero_list.reverse()
    print(hero_list)

    # 升序排列
    score_list = [80, 90, 82, 70, 55, 98, 63]
    score_list.sort()
    print(score_list)

    # 降序排列
    score_list = [80, 90, 82, 70, 55, 98, 63]
    score_list.sort(reverse=True)
    print(score_list)

# list_add()
# list_search()
# list_del()
# list_modify()

'''
字典增删查改
'''
def dict_add():
    """
    字典添加
    :return:
    """
    s = {}
    s['name'] = '张三'
    s['age'] = 30
    print(s)
    s['age'] = 40
    print(s)
    s.setdefault('sex', '男') # 如果key不存在则新增
    print(s)

def dict_del():
    """
    字典删除
    :return:
    """
    # 删除整个字典
    s = {'name': '张三', 'age': 50}
    del s
    # print(s)

    # 删除指定key对应键值对
    s = {'name': '张三', 'age': 50}
    del s['name']
    print(s)

    # 删除指定键值对并返回值
    s = {'name': 'zs', 'age': 20, 'height': 180, 'score': 10}
    s.pop('name')
    print(s)
    s.pop('age', 20)
    print(s)

    # 删除字典中最后一个键值对并返回
    s = {'name': 'zs', 'age': 20, 'height': 180, 'score': 10}
    kv = s.popitem()
    print(kv)

    # 删除字典中所有键值对
    s = {'name': 'zs', 'age': 20, 'height': 180, 'score': 10}
    s.clear()
    print(s)


def dict_modify():
    """
    字典修改
    :return:
    """
    s = {'name': 'zs', 'age': 20, 'height': 180, 'score': 10}

    # 修改键值对的值
    s['age'] = 30
    print(s)

    # 把s1的键值对更新到s里（s中存在的key改为s1中的值,s中不存在的key则添加）
    s1 = {'name': '张三', 'sex': True}
    s.update(s1)
    print(s)


def dict_search():
    """
    字典查询
    :return:
    """
    s = {'name': 'zs', 'age': 20, 'height': 180, 'score': 10}

    # 直接通过key查找
    print(s['name'])

    # 用get()通过key查找
    print(s.get('name'))
    print(s.get('nickname')) # 不存在则返回默认值None
    print(s.get('nickname', '小明')) # 不存在则返回指定默认值'小明'

    # 以可遍历的形式返回字典中的所有键
    keys = s.keys()
    print(type(keys))
    print(keys)

    # 以可遍历的形式返回字典中的所有值
    values = s.values()
    print(type(values))
    print(values)

    # 以可遍历的形式返回可遍历的(键, 值)元组数组
    items = s.items()
    print(type(items))
    print(items)

# dict_add()
# dict_del()
# dict_modify()
# dict_search()

def str_cut():
    """
    字符串切片
    :return:
    """
    num_str = "0123456789"

    # 截取从 2 ~ 5 位置 的字符串
    print(num_str[2:6])

    # 截取从 2 ~ 末尾的字符串
    print(num_str[2:])

    # 截取从 开始~ 5 位置 的字符串
    print(num_str[:6])

    # 截取完整的字符串
    print(num_str)

    # 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])

    # 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])

    # 截取从 2 ~ 末尾 - 1的字符串
    print(num_str[2:-1])

    # 截取字符串末尾两个字符
    print(num_str[-2:])

    # 字符串的逆序（面试题）
    print(num_str[::-1])

# str_cut()

def use_enumerate():
    """
    使用enumerate把seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 变为一个字典
    :return:
    """
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    seasons_dict = {}
    for key, value in enumerate(seasons):
        seasons_dict[key] = value
    print(seasons_dict)

use_enumerate()