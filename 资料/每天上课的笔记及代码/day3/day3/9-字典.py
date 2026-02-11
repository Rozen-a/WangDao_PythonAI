# 作者: 王道 龙哥
# 2026年02月09日14时51分19秒
# xxx@qq.com

def use_dict():
    # 定义一个有键值对的字典
    student = {"name": "bob", "age": 20, "height": 180}
    print(student)

    print(student['height'])


def dict_add():
    s = {}
    s['name'] = '张三'
    s['age'] = 30
    print(s)
    s['age'] = 50
    print(s)
    s.setdefault('age', 21)  # key存在就不放，如果key不在，才新增
    print(s)


def dict_del():
    s = {'name': '张三', 'age': 50}
    del s  # 为了释放空间，所以del变量
    # print(s)
    s = {'name': '张三', 'age': 50}
    del s['name']
    print(s)
    # del s['height']
    age = s.pop('age')
    print(age)

    s = {'name': 'zs', "age": 20, "height": 180, "score": 10}

    # score:10 是最后添加的，这里返回它
    kv = s.popitem()
    print(kv)

    s.clear()
    print(s)


def dict_query():
    """
    字典查询
    :return:
    """
    s = {'name': 'zs', "age": 20, "height": 180, "score": 10}
    print(s.get('sex', True))  # 拿不到sex，返回默认True
    for key in s:
        print(key)
    print('-' * 50)
    for v in s.values():
        print(v)
    print('-' * 50)
    for k, v in s.items():  # 最常用
        print(k, v)

    s['age'] = s['age'] + 2
    print(s)
    print(max(s)) #不会对字典进行max的


def dict_modify():
    s = {'name': 'zs', "age": 20, "height": 180, "score": 10}
    s1={'name': '张三','sex':True}
    s.update(s1)
    print(s)

# use_dict()
# dict_add()
# dict_del()
dict_query()
# dict_modify()