# 作者: 王道 龙哥
# 2026年02月11日09时56分31秒
# xxx@qq.com
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有属性（余额）

    # 提供公开接口查询余额
    def get_balance(self):
        return self.__balance

    # 提供公开接口存款
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # 提供公开接口取款
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return amount
        return 0


# 1. 要求学生的年龄在10-30之间，不在这个区间就赋予默认值
# 2. 要求学生的成绩在0-100之间，不在则赋予默认值
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__age = 20  # 赋予年龄默认值20
        self.__score = 80  # 赋予成绩默认值80

    def __str__(self):
        return f"name:{self.name}, gender:{self.gender}, age:{self.__age}, score:{self.__score}"

    # 定义获取年龄的方法
    def get_age(self):
        return self.__age

    # 定义修改年龄的方法
    def set_age(self, age):
        if 30 >= age >= 10:
            self.__age = age

    # 定义获取成绩的方法
    def get_score(self):
        return self.__score

    # 定义设置成绩的方法
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score


class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 20
        self._score=98.5

    def __secret(self):
        return self.__age

    def boy_friend(self):
        return self.__secret()


if __name__ == '__main__':
    # account = BankAccount(2000)
    # print(account.get_balance())
    s = Student('小王', '男')
    s.set_age(25)
    print(s.get_age())
    xiaoli=Girl('小丽')
    print(xiaoli.boy_friend())
