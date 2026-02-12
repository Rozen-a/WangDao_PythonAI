# 作者: 王道 龙哥
# 2026年02月12日16时41分36秒
# xxx@qq.com
import os

# os.rename('dir/file4','dir/file5')

# os.remove('dir/file5')

print(os.listdir('.'))

# os.mkdir('dir1')
# os.rmdir('dir1')
print(os.path.isdir('dir'))

print(os.getcwd())
os.chdir('dir')
print(os.getcwd())
