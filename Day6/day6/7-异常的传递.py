# 作者: 王道 龙哥
# 2026年02月12日10时50分36秒
# xxx@qq.com

def demo1():
    content = input("请输入一个整数:")
    num = int(content)
    print(f'demo1{num}')
    return num


def demo2():
    demo1()
    print('demo1 执行成功')


if __name__ == '__main__':
    # demo2()
    try:
        demo2()
    except Exception as e:
        print(e)
