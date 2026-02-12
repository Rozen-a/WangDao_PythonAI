# 作者: 王道 龙哥
# 2026年02月12日11时09分18秒
# xxx@qq.com

def calculate_average(numbers):
    assert len(numbers)>0,'列表长度没有大于0'
    return sum(numbers)/len(numbers)

try:
    print(calculate_average([]))
except Exception as e:
    print(e)