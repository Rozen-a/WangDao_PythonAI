# 作者: 王道 龙哥
# 2026年02月09日09时47分28秒
# xxx@qq.com

def use_str():
    # 定义字符串
    s1 = 'abc'  # 使用单引号
    s2 = '12345'
    s3 = "你好,王道考研"  # 使用双引号
    s4 = "god bless you"
    s5 = """				
    我是安卓人'
        你是苹果人"
            他是鸿蒙人
                我们都是地球人
    """
    print(s5)

    s6 = 'I\'m a "singer'  # 转义字符,\是用来进行转义的
    print(s6)


def char_study():
    char_num = ord('A')
    print(char_num)
    char = chr(char_num)
    print(char)


def big_small():
    """
    大写变小写
    :return:
    """
    char = input()
    print(chr(ord(char) + 32))


def str_iter():
    for i in 'wangdao':
        print(i)

# use_str()
# char_study()
# big_small()
str_iter()