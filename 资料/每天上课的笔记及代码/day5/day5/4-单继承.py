# 作者: 王道 龙哥
# 2026年02月11日10时32分46秒
# xxx@qq.com
class Father:
    def __init__(self,gender):
        self.gender = gender

    def walk(self):
        print('爱好散步行走')


class Son(Father):
    pass

s=Son('男')
print(s.gender)
s.walk()