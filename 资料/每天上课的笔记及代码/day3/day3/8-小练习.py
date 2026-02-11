# 作者: 王道 龙哥
# 2026年02月09日14时38分57秒
# xxx@qq.com

def list_range():
    """
    数字8，生成nums列表，元素值为1~8
    :return:
    """
    num = int(input('请输入数字'))
    new_list = []
    for i in range(1, num + 1):
        new_list.append(i)
    print(new_list)


import random


def arrange_room():
    class_room = [[], [], []]
    teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for t in teacher:
        i = random.randint(0, 2)  # 随机得到某个教室的下标
        temp = class_room[i]
        temp.append(t)
    print(class_room)


# list_range()
arrange_room()
