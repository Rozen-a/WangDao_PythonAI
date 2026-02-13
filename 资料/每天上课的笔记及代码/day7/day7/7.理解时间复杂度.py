# 作者: 王道 龙哥
# 2026年02月13日16时19分03秒
# xxx@qq.com

def f(n):
    for i in range(2 * n + 3):
        pass


def f2(n):
    for i in range(5 * n):
        for j in range(n):
            for k in range(n):
                pass
    for i in range(3 * n):
        pass


if __name__ == '__main__':
    f(1000000)

