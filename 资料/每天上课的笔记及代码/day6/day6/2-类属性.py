# 作者: 王道 龙哥
# 2026年02月12日09时25分23秒
# xxx@qq.com
class Student:
    school = '北京大学'

    def __init__(self, name, age):
        # 对象属性：通过self绑定到当前对象
        self.name = name  # 每个学生的姓名不同
        self.age = age  # 每个学生的年龄不同


# 创建两个对象，对象属性独立
stu1 = Student("张三", 20)
stu2 = Student("李四", 19)

print(stu1.name)  # 输出：张三（stu1的专属属性）
print(stu2.age)  # 输出：19（stu2的专属属性）
print(id(stu1))
stu1.name = '王五'
print(id(stu1))

print('-' * 50)
print(Student.school)
print(stu1.school)
print(stu2.school)
# stu1.school='清华大学'  #给stu1对象增加了一个对象属性叫school
Student.school='清华大学'
print(Student.school)
print(stu1.school)
print(stu2.school)
