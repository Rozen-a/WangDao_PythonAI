# 作者: 王道 龙哥
# 2026年02月08日16时13分12秒
# xxx@qq.com

def use_if():
    score = 92
    if score > 60:
        print('小明及格了')
        print('他很开心')
        if score > 90:
            print('小明优秀')
    else:
        print('小明不及格')

    print('无论是否及格都会看到')


def use_elif():
    score = 82
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    else:
        print('C')


def use_compare():
    """
    比较的连写
    :return:
    """
    num = -3
    if 1 < num < 5:
        print('num is ok')


# use_if()
# use_elif()
use_compare()
