# 作者: 王道 龙哥
# 2026年02月09日10时43分10秒
# xxx@qq.com

str1 = 'dbjakbdj123bkabdjka12bjkabdjk123bjadbja123bfegbrk123;jfpej12'
print(len(str1))
print(str1.find('123'))

start = 0
count = 0
while start <= len(str1):
    start_pos = str1.find('123', start)
    if start_pos >= 0:
        count += 1
        start = start_pos + 1
    else:
        break
print(count)

str2=str1.replace('123','456')
print(str2)
print(str1)

print('-'*50)
str3='hello world how are you'
print(str3.split())
str4='hello,world,how,are,you'
str_list=str4.split(',')
print(str_list)
print('-'.join(str_list))