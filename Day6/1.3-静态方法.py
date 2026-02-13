"""
1.3 练习静态方法
"""
class MathHelper:
    @staticmethod  # 修饰静态方法（纯功能逻辑）
    def is_even(num):  # 可传普通参数，无需 self 或 cls
        return num % 2 == 0

    @staticmethod
    def average(a, b):
        return (a + b) / 2


math = MathHelper()
print(math.is_even(10))
print(math.average(5, 6))