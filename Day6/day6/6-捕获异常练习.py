# 作者: 王道 龙哥
# 2026年02月12日10时39分04秒
# xxx@qq.com
#掌握如何捕获异常信息

try:
    num = int(input('请输入一个整数'))
    result = 8 / num
    print(result)
except ValueError:
    print('请输入整数')
except ZeroDivisionError:
    print('不能输入0')
except Exception as e:
    print(e)  # 打印异常信息，如果是项目，就把异常信息记录到文件里去
