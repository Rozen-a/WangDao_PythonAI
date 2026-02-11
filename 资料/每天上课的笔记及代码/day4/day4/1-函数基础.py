# 作者: 王道 龙哥
# 2026年02月10日09时37分43秒
# xxx@qq.com
def get_sum(a, b):
    return a + b


result = get_sum(10, 20)
print(result)


def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def testA():
    print('---- testA start----')
    # 嵌套调用函数B
    testB()
    print('---- testA end----')


testA()
