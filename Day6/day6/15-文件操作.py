# 作者: 王道 龙哥
# 2026年02月12日15时44分55秒
# xxx@qq.com
import os


# print(os.getcwd())

def use_r():
    # 写代码，都需要使用相对路径。相对路径，是相对于当前进程的路径
    f = open('dir/file.txt', 'r', encoding='utf8')
    txt = f.read()
    print(type(txt))
    print(txt)
    f.close()


def use_w():
    # 写代码，都需要使用相对路径。相对路径，是相对于当前进程的路径
    f = open('dir/file1.txt', 'w', encoding='utf8')  # 只能写，不能读，会清空文件，文件不存在会创建
    f.write('今天天气很好')
    f.close()


def use_r2():
    # 写代码，都需要使用相对路径。相对路径，是相对于当前进程的路径
    f = open('dir/file2.txt', 'r+', encoding='utf8')  # 打开文件时，光标在开头
    f.write('今天天气很好')
    f.close()


def use_a2():
    f = open('dir/file2.txt', 'a+', encoding='utf8')
    f.write('坚持练习持续提升')
    f.close()


def use_readline():
    f = open('dir/file3.txt', 'r+', encoding='utf8')
    while True:
        txt = f.readline()  # 每次读一行，读空如何写
        if not txt:
            break
        print(txt, end='')
    f.close()


def use_readlines():
    f = open('dir/file3.txt', 'r+', encoding='utf8')
    str_list = f.readlines()
    print(str_list)
    f.close()


def use_with():
    with open('dir/file.txt', 'r', encoding='utf8') as f:
        print(f.read())

# use_r()
# use_w()
# use_r2()
# use_a2()
# use_readline()
# use_readlines()
use_with()
