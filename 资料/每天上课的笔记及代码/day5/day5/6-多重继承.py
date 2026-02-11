# 作者: 王道 龙哥
# 2026年02月11日11时00分35秒
# xxx@qq.com
# 父类1
class Flyable:
    def fly(self):
        print("会飞")


# 父类2
class Swimmable:
    def swim(self):
        print("会游泳")


# 子类继承多个父类
class Duck(Flyable, Swimmable):
    pass


duck = Duck()
duck.swim()
duck.fly()
