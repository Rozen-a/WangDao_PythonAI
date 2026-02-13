# 作者: 王道 龙哥
# 2026年02月12日10时29分22秒
# xxx@qq.com

def devide(a, b):
    try:
        result = a / b
        print(f'{result}')
    except ZeroDivisionError:
        print('除0异常')
    else:
        print('计算成功')
        return result
    finally:
        # 无论是否异常，都会执行,不受return影响
        print("除法运算结束\n")


result=devide(1, 2)
print(f'函数外 {result}')