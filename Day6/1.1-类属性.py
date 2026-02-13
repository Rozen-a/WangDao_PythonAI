"""
1.1 练习类属性
"""
class Student:
    school = '北京大学'

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student('张三', 20)
stu2 = Student('李四', 21)

# 同类所有对象共享类属性
print(stu1.school)
print(stu2.school)
print(Student.school)
print()

# 使用类名修改类属性，同步变化
Student.school='清华大学'
print(stu1.school)
print(stu2.school)
print(Student.school)
print()

# 使用对象名修改类属性，相当于给该对象增加了一个同名对象属性
stu1.school='北京大学'# 只有stu1的school属性变化
print(stu1.school)
print(stu2.school)
print(Student.school)