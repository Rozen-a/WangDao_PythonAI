# 作者: 王道 龙哥
# 2026年02月09日16时16分16秒
# xxx@qq.com

def compare():
    """
    列表 字符串，比较
    :return:
    """
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [1, 2, 4]
    list_d = [1, 5]
    list_e = [1, 3, 2]

    print(list_a == list_b)
    print(list_d > list_e)

    print('hello' > 'how')


def use_reversed():
    my_list = ['a', 'b', 'e', 'd']
    new_reverseiterator = reversed(my_list)
    print(my_list)
    # print(list(new_reverseiterator))
    for i in new_reverseiterator:
        print(i)


def use_enumerate():
    word_list = ['hello', 'today', 'good', 'day']
    word_dict = {}
    for index, word in enumerate(word_list):  # 遍历可迭代对象时，每个位置依次给与编号
        word_dict[word] = index
    print(word_dict)


# compare()
# use_reversed()
use_enumerate()
