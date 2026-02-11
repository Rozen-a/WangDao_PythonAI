# 作者: 王道 龙哥
# 2026年02月08日14时59分19秒
# xxx@qq.com

def use_int():
    data = input('请输入数据')
    print(data)
    print(type(data))

    # TypeError 不支持对应类型的运算
    num = int(data) + 1
    print(num)


def use_float():
    data = input('请输入数据')
    print(data)
    print(type(data))

    score = float(data)
    print(score)
    new_score = int(score)
    print(new_score)


# use_int()
use_float()
