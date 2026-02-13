"""
3.传递参数file1，通过sys.argv[1]打开文件，读取里边的内容并打印
如果传递的参数是file2，程序同样可以打印file2的文件内容
"""
import sys
print(sys.argv) # 打印传参

with open(sys.argv[1], 'r', encoding='utf8') as f1:  # 通过传参打开文件
    content = f1.read()
    print(content)

with open(sys.argv[2], 'r', encoding='utf8') as f2:
    content = f2.read()
    print(content)