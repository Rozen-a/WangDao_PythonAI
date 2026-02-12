# 作者: 王道 龙哥
# 2026年02月12日09时18分08秒
# xxx@qq.com
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.__age=age


class Dog(Animal):
    def get_age(self):
        print(self.__age)


dog=Dog('小黄',20)
print(dog.name)
# dog.get_age() #执行会报错
