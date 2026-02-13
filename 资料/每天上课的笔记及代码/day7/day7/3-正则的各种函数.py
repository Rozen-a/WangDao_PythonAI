# 作者: 王道 龙哥
# 2026年02月13日11时16分46秒
# xxx@qq.com
import re


def use_search():
    text = "我的手机号：13812345678，备用号：13987654321"
    pattern = r"1[34578]\d{9}"  # 不限制位置，只匹配手机号格式

    result = re.search(pattern, text)
    if result:
        print(result.group())
        print("位置：", result.span())
    else:
        print('没匹配')


def use_findall():
    text = "我的手机号：13812345678，备用号：13987654321"
    pattern = r"1[34578]\d{9}"

    phones = re.findall(pattern, text)
    print("所有手机号：", phones)  # 输出：所有手机号：['13812345678', '13987654321']


def use_sub():
    text = "这个内容是垃圾，不要传播垃圾信息"
    pattern = r"垃圾"
    new_text = re.sub(pattern, '*', text, 1)
    print(new_text)


def use_sub2():
    text = "13812345678"

    # ()： 表示分组匹配，将内部字符视为一个整体，后续可以提取
    pattern = r"(\d{3})(\d{4})(\d{4})"  # 分3个分组（前3/中4/后4位）
    new_text = re.sub(pattern, r'\1 \2 \3', text)
    print(new_text)


def add(str_num) -> str:
    # str_num 是re.search(pattern,text) 返回值
    return str(int(str_num.group()) + 1)


def use_sub3():
    text = "发射神舟11号"
    pattern = r'\d+'
    # add就是回调函数
    new_text = re.sub(pattern, add, text)
    print(new_text)

    new_text = re.sub(pattern, lambda s: str(int(s.group()) + 1), text)
    print(new_text)


def use_split():
    text = "apple banana,orange;grape"
    pattern = r"[ ,;]"  # 匹配空格、逗号、分号中的任意一个
    result = re.split(pattern, text)
    print(result)


if __name__ == '__main__':
    # use_search()
    # use_findall()
    # use_sub()
    # use_sub2()
    # use_sub3()
    use_split()
