# 作者: 王道 龙哥
# 2026年02月11日11时02分39秒
# xxx@qq.com
class A:  # 祖父类
    def say(self):
        print("A的say方法")


class B(A):  # 父类1，继承A
    def say(self):
        print("B的say方法")


class C(A):  # 父类2，继承A
    def say(self):
        print("C的say方法")


class D(B, C):  # 子类，继承B和C
    pass  # 未重写say方法

d=D()
d.say()
print(D.__mro__)
