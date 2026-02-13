# 作者: 王道 龙哥
# 2026年02月12日09时33分12秒
# xxx@qq.com
class Tool:
    # 类属性：记录工具总数
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_total(cls):
        """
        使用了classmethod装饰的方法，是类方法，cls是类名
        :return:
        """
        print(f'工具总数{cls.count}')


# 创建对象后，类属性变化
tool1 = Tool("锤子")
tool2 = Tool("螺丝刀")
print(Tool.count)
# 要使用类名来调用类方法
Tool.show_total()

print('-' * 50)


class MathHelper:
    # 静态方法：纯功能逻辑（判断是否为偶数）
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    # 静态方法：纯功能逻辑（计算平均值）
    @staticmethod
    def average(a, b):
        return (a + b) / 2


math = MathHelper()
print(math.is_even(10))
print(math.average(5,6))
