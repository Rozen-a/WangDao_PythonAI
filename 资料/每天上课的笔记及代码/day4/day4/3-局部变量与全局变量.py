# 作者: 王道 龙哥
# 2026年02月10日09时52分38秒
# xxx@qq.com

# 尽量避免使用全局变量
b = 50


def func():
    a = 100
    print(f'a {a}')
    global b  # 如果在函数内要修改全局变量的值，就需要使用global
    print(f'全局变量 b {b}')
    b = 30
    print(f'全局变量 b {b}')


def func1():
    b = 20  # 局部变量不要和全局变量重名
    print(f'局部变量 b {b}')


if __name__ == '__main__':
    # func()
    func1()
