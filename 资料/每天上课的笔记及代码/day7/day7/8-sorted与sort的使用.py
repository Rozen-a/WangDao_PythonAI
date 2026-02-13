# 作者: 王道 龙哥
# 2026年02月13日16时39分37秒
# xxx@qq.com


def use_sorted1():
    nums = [3, 1, 4, 2]
    sorted_nums = sorted(nums)
    print("原列表：", nums)  # 原列表：[3, 1, 4, 2]（不变）
    print("排序后：", sorted_nums)  # 排序后：[1, 2, 3, 4]（新列表）


def sorted_str_list():
    words = ["apple", "banana", "cat", "dog"]
    # for i in words  i传给len
    # 比较 len(i) >len(i1)
    # key=len：按字符串长度排序
    sorted_words = sorted(words, key=len)
    print(sorted_words)


def get_age(x):
    return x['age']


def sorted_list_dict():
    students = [
        {"name": "Alice", "age": 18},
        {"name": "Bob", "age": 16},
        {"name": "Charlie", "age": 20}
    ]
    result = sorted(students, key=lambda student: student['age'], reverse=True)
    print(result)
    # 所以排序也可以替换为：
    sorted_students = sorted(students, key=get_age)
    print(sorted_students)


def sorted_more_column():
    """
    排序多列
    :return:
    """
    tup = [(3, 5), (1, 2), (2, 4), (3, 1), (1, 3)]
    result = sorted(tup, key=lambda x: (x[0], -x[1]))
    print(result)


def sorted_dict_more():
    """
    排序字典中多个键
    :return:
    """
    students = [
        {"name": "Bob", "age": 18, 'score': 66},
        {"name": "Alice", "age": 18, 'score': 62},
        {"name": "Charlie", "age": 20, 'score': 77}
    ]
    # key返回元组(age, -len(name))：先按age升序，再按name长度降序
    sorted_students = sorted(students, key=lambda x: (x["age"], x['score']))
    print(sorted_students)


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        """
        与str功能一致，但是更牛的打印函数
        :return:
        """
        return f"Student(name={self.name}, age={self.age}, score={self.score})"


def sorted_object():
    students = [
        {"name": "Bob", "age": 18, 'score': 66},
        {"name": "Alice", "age": 18, 'score': 62},
        {"name": "Charlie", "age": 20, 'score': 77}
    ]

    # 转换,列表中放对象
    students = [Student(**stu) for stu in students]

    print(students)
    result = sorted(students, key=lambda x: x.score)
    print(result)


if __name__ == '__main__':
    # use_sorted1()
    # sorted_str_list()
    # sorted_list_dict()
    # sorted_more_column()
    # sorted_dict_more()
    sorted_object()
