"""
练习私有属性和私有方法
"""


# 银行案例
class BankAccount:
    """
    银行账户类
    """

    def __init__(self, balance):
        self.__balance = balance  # 私有属性（余额）

    # 提供公开接口查询余额
    def get_balance(self):
        return self.__balance

    #提供公开接口存款
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    #提供公开接口取款
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0

# if __name__ == '__main__':
#     account = BankAccount(1000) # 创建银行账户
#     print(account.get_balance()) # 通过接口查询余额
#     account.deposit(500) # 存款
#     print(account.get_balance())
#
#     # 尝试直接访问私有属性
#     print(account.__balance) # 报错


# 学生案例
# 定义一个学生类
# 1. 要求学生的年龄在10-30之间，不在这个区间就赋予默认值
# 2. 要求学生的成绩在0-100之间，不在则赋予默认值
class Student:
    """
    学生类
    """
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__age = 20 # 默认年龄20
        self.__score = 80 # 默认成绩80

    def __str__(self):
        return f'name:{self.name}, gender:{self.gender}, age:{self.__age}, score:{self.__score}'

    # 获取年龄
    def get_age(self):
        return self.__age

    # 修改年龄
    def set_age(self, age):
        if 30 >= age >= 10:
            self.__age = age


    # 获取成绩
    def get_score(self):
        return self.__score

    # 设置成绩
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score  = score


# if __name__ == '__main__':
#     s = Student('小王', '男')
#     s.set_age(25)
#     print(s.get_age())

# 私有方法练习
class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 20 # 私有属性
        self._score = 98.5 # 受保护的属性

    # 私有方法
    def __secret(self):
        return self.__age

    def boy_friend(self):
        return self.__secret() # 调用私有方法


if __name__ == '__main__':
    xiaoli = Girl('小丽')
    print(xiaoli.boy_friend())



