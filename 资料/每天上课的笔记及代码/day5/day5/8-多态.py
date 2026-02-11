# 作者: 王道 龙哥
# 2026年02月11日11时09分41秒
# xxx@qq.com

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        # 父类方法：定义接口
        pass


# 2. 子类（继承+重写）
class Dog(Animal):
    def make_sound(self):  # 重写父类方法
        print("汪汪叫")


class Cat(Animal):
    def make_sound(self):  # 重写父类方法
        print("喵喵叫")


class Duck(Animal):
    def make_sound(self):  # 重写父类方法
        print("嘎嘎叫")


class Tiger(Animal):
    def make_sound(self):
        print('嗷嗷叫')


# 3. 统一调用（父类引用指向子类对象）
def animal_sound(animal: Animal):  # 参数声明为父类类型
    animal.make_sound()
#
dog=Dog()
cat=Cat()
animal_sound(dog)
animal_sound(cat)
t = Tiger()
animal_sound(t)