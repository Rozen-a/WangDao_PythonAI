# 作者: 王道 龙哥
# 2026年02月10日15时38分53秒
# xxx@qq.com
import sys

sys.setrecursionlimit(1000001)


# f(n)=n+f(n-1)

def f(n):
    if n == 1:
        return 1
    return n + f(n - 1)


print(f(1000000))


def step(n):
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)


for n in range(1,10):
    print(step(n),end=' ')