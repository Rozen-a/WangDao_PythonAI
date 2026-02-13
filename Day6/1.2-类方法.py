"""
1.2 练习类方法
"""
class Tool:
    count = 0 # 记录对象数

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod # 修饰类方法
    def show_total(cls):
        print(f'工具总数{cls.count}')


tool1 = Tool('锤子')
tool2 = Tool('螺丝刀')
print(Tool.count)

# 使用类名调用类方法
Tool.show_total()