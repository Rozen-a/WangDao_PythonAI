"""
2.通过try进行异常捕捉，确保输入的内容一定是一个整型数，
然后判断该整型数是否是对称数，12321就是对称数，
123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常
"""
try:
    user_input = input('请输入一个整数：')
    num = int(user_input)
    if user_input == user_input[::-1]:
        print(f'{user_input}是对称数')
    else:
        raise Exception(f'{user_input}不是对称数')

except ValueError:
    print('错误：输入的不是整数')
except Exception as e:
    print(f'错误：{e}')
