# 作者: 王道 龙哥
# 2026年02月09日11时08分34秒
# xxx@qq.com

def use_append():
    """
    列表添加
    :return:
    """
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.append('龙哥')
    print(name_list)
    city_list = ["北京", "上海", "广州", "深圳"]
    new_city_list = ["成都", "杭州", "重庆", "武汉"]

    city_list.extend(new_city_list)
    print(city_list)

    name_list.insert(1, 'lele')
    print(name_list)

    name_list[1] = 'qiqi'
    print(name_list)

    num_list = [0] * 10  # 初始化一个列表，里边都是为0
    num_list[1] = 2
    print(num_list)


def use_query():
    """
    列表查询
    :return:
    """
    my_list = ['小李', '小明', '嘉豪', '小张', '嘉豪', '老王', '老李', '楚云飞', '嘉豪']
    print(my_list.index('小明'))
    print(my_list.index("嘉豪", 3))
    print(my_list.index("嘉豪", 6, 10))

    print('-' * 50)
    print(my_list.count('嘉豪'))

    print('小李' in my_list)
    print('小李' not in my_list)


def use_list_del():
    """
    列表删除
    :return:
    """
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    del hero_list[2]
    print(hero_list)
    hero_list.pop(1)
    print(hero_list)
    print('-' * 50)
    my_list = ['小李', '小明', '嘉豪', '小张', '嘉豪', '老王', '老李', '楚云飞', '嘉豪']
    my_list.remove('嘉豪')
    print(my_list)
    my_list.clear()
    print(my_list)


def del_all_element():
    """
    删除列表中等于某值的元素
    :return:
    """
    my_list = ['小李', '小明', '嘉豪', '嘉豪', '老王', '老李', '楚云飞', '嘉豪']
    i = 0
    while i < len(my_list):
        if my_list[i] == '嘉豪':
            del my_list[i]  # 删除某个元素时，i不加1
        else:
            i += 1
    print(my_list)


def list_modify():
    """
    列表修改
    :return:
    """
    hero_list = ['吴用', '宋江', '鲁智深', '林冲', '花荣', '晁盖']
    hero_list[0] = "智多星"
    print(hero_list)
    hero_list.reverse()
    print(hero_list)
    num_list = [8, 5, 3, 2, 6]
    num_list.sort(reverse=True)
    print(num_list)


def special_list():
    list1 = [1, 2, 3]
    list2 = [5, 6, 7, 8, 9]
    list2[2:2] = list1  # 把列表插入到某个列表中间
    print(list2)


# use_append()
# use_query()
# use_list_del()
# del_all_element()
# list_modify()
special_list()
