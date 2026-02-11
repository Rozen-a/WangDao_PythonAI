# 作者: 王道 龙哥
# 2026年02月08日14时39分15秒
# xxx@qq.com

def study_print1():
    print('hello', end=' ')
    print('world')
    print('how\nareyou')

    print("haha")

    # NameError
    # name='zhangsan'
    # print(name1)

    print('hello')
    print('world')


def study_print2():
    """
    学习格式化输出
    :return:
    """
    age = 10
    print("我今年%d岁了" % age)

    name = '老天师'
    print("%s, 你败过吗？" % name)

    score = 88.5
    print("我叫蜡笔小新，今天考了%5.2f分" % score)

    # 多占位符
    name = '韩立'
    age = 20
    score = 88.36
    print('我叫%s, 我今年%d岁了, 在宗门小比中，我得了%f分' % (name, age, score))

    # 插值表达式,不需要花时间记住输出格式问题
    print(f'我叫{name}, 我今年{age}岁了, 在宗门小比中，我得了{score:.3f}分')


# study_print1()
study_print2()
