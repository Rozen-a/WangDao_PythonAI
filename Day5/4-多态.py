"""
练习多态案例
"""
from abc import ABC, abstractmethod


class Animal(ABC):  # 抽象类

    @abstractmethod
    def make_sound(self):  # 抽象方法
        pass


class Dog(Animal):
    def make_sound(self):  # 重写父类抽象方法
        print('汪汪叫')


class Cat(Animal):
    def make_sound(self):
        print('喵喵叫')


class Duck(Animal):
    def make_sound(self):
        print('嘎嘎叫')


class Tiger(Animal):
    def make_sound(self):
        print('嗷嗷叫')


# 多态：使用父类类型统一调用
def animal_sound(animal: Animal):
    animal.make_sound()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    tiger = Tiger()

    # 根据不同的子类类型调用不同的方法
    animal_sound(dog)
    animal_sound(cat)
    animal_sound(tiger)