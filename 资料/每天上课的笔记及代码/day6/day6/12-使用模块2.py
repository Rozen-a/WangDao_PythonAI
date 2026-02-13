# 作者: 王道 龙哥
# 2026年02月12日14时11分04秒
# xxx@qq.com

# 避免自身的模块名和系统的模块名重名
import my_module as m
from my_module import Calculator
# from my_module1 import Calculator
# from my_module import *  #不推荐

print(m.add(1, 2))

cal = Calculator()
print(cal.multiply(3, 4))
print(f'm.pi {m.pi}')
# print(m.i) #不会导入__main__的代码


print(__name__)
print(m.__name__)
