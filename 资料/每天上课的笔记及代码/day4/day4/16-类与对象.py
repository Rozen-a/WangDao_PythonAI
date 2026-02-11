# 作者: 王道 龙哥
# 2026年02月10日16时36分06秒
# xxx@qq.com


class Dog:
    def bark(self):
        print('汪汪叫')


dog1 = Dog()
dog1.bark()

print('-' * 50)


# object是所有类的基类
class Car(object):
    def __init__(self, name, color1):
        """
        init是为了初始化对象属性
        :param name:
        :param color1:
        """
        self.name = name  # 给对象新加了一个属性
        self.color = color1  # 给对象新加了一个属性
        # self.size=None

    def run(self):
        print(f'{self.name}车在跑')

    # def oil(self):
    #     print(f'{self.name}车在加油')
    def __str__(self):
        """
        打印对象时，会打印这个函数的返回值
        :return:
        """
        return f'{self.name}---{self.color}'

    def __del__(self):
        print(f'{self.name}要被销毁了')


# Car('小米') 这个过程，叫 实例化，对象是类的实例
xiaomi = Car('小米', 'Red')
wenjie = Car('问界', 'Black')
# xiaomi.color='Red' # 这种写法是不规范的

xiaomi.run()
wenjie.run()
print('-' * 50)
print(xiaomi)
print(xiaomi.name)
print(xiaomi.color)
# 不存在的属性或方法，会出现 AttributeError
# print(xiaomi.size)
# xiaomi.oil()
del xiaomi

print(wenjie)
print(wenjie.name)
print(wenjie.color)
