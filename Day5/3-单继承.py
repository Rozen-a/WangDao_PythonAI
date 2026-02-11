"""
练习单继承案例
"""
# 父类
class Animal:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def eat(self):
        print(f'{self.name}安静的在吃东西')


# 子类
class Dog(Animal):
    # 重写init方法
    def __init__(self, name, size, color):
        super().__init__(name, size) # 使用super调用父类方法
        self.color = color

    # 新增子类独有的方法
    def bark(self):
        print(f'{self.name}在汪汪叫')

    # 重写eat方法
    def eat(self):
        super().eat()
        print(f'{self.name}帅气的在吃东西')


# 子类
class Cat(Animal):
    def catch(self):
        print(f'{self.name}爬房顶')


# 使用子类
dog = Dog('旺财', 50, '黄色')
cat = Cat('咪咪', 30)
dog.eat()
dog.bark()
print(dog.color)
cat.eat()