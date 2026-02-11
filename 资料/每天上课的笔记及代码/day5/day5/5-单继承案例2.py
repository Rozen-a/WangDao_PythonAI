# 作者: 王道 龙哥
# 2026年02月11日10时36分43秒
# xxx@qq.com
class Animal:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def eat(self):
        print(f"{self.name} 安静的 在吃东西")


# 子类（派生类），通过`()`指定父类
class Dog(Animal):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    # 新增子类独有的方法
    def bark(self):
        print(f"{self.name}在汪汪叫")

    def eat(self):
        """
        子类中有对应的方法，就会直接覆盖父类的方法
        :return:
        """
        # super()是匿名父类
        super().eat()
        print(f"{self.name} 帅气的 在吃东西")


class Cat(Animal):
    def catch(self):
        print(f"{self.name}爬房顶")


dog = Dog('旺财', 50, '黄色')
cat = Cat('咪咪', 30)
dog.eat()
print(dog.color)
cat.eat()
