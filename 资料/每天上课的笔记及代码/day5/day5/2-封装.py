# 作者: 王道 龙哥
# 2026年02月11日09时52分06秒
# xxx@qq.com
class Person:
    # 封装属性（数据）
    def __init__(self, name, age):
        self.name = name  # 姓名属性
        self.age = age  # 年龄属性

    # 封装方法（操作数据的函数）
    def get_info(self):
        return f"姓名：{self.name}，年龄：{self.age}"

    def grow_up(self):
        self.age += 1  # 只能通过方法修改年龄


# 使用封装的类
p = Person("张三", 20)
print(p.get_info())  # 通过接口访问 → 姓名：张三，年龄：20
p.grow_up()  # 通过方法修改数据
print(p.get_info())  # 姓名：张三，年龄：21

