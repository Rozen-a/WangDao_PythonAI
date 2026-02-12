# 作者: 王道 龙哥
# 2026年02月12日11时02分00秒
# xxx@qq.com

def get_password():
    password = input("请输入密码:")
    if len(password) < 8:
        raise Exception('密码长度小于8位')
    return password


try:
    password = get_password()
    print(f'密码是{password}')
except Exception as e:
    print(f'日志信息 {e}')

