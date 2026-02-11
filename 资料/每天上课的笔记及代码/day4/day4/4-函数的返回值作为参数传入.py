# 作者: 王道 龙哥
# 2026年02月10日10时30分25秒
# xxx@qq.com
# 演示 1. 函数的返回值可以作为 (另一个函数的)参数进行传递.
def fun1():
    return 100  # 返回1个结果 100


def fun2(num):  # 需要1个参数
    print(num)


ret = fun1()
fun2(ret)

fun2(fun1())
