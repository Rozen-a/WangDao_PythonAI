# 作者: 王道 龙哥
# 2026年02月10日10时53分16秒
# xxx@qq.com


def print_info(name, age=0, gender=False):
    print(f'姓名{name}')
    print(f'年龄{age}')
    print(f'性别{gender}')


# 位置参数使用
print_info('王小道', 20, True)
# print_info( 20,'王小道', True) #不对
print('-' * 50)
# 关键字调用方式
print_info(name='王小道', age=20, gender=True)
print_info(age=20, name='王小道', gender=True)

print('-' * 50)
# 使用缺省参数(参数有默认值）
print_info('王小道', 20)
print_info('王小道', 20, True)

print('-' * 50)
#只给gender缺省参数传数据
print_info('王小道', gender=True)
