# Python基础笔记

## Day2

### 1. 现字符串插值的方式

| **方法**                              | **基本语法**                                                 | **主要优点**                                     |
| :------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------ |
| **f**-**string** (格式化字符串字面值) | `f"Hello, {name}"`                                           | 语法简洁直观，**执行效率高**，支持内嵌复杂表达式 |
| **str.format()** 方法                 | `"Hello, {}".format(name)`<br>` "Hello,{name}".format(name=name)` | 功能灵活强大，兼容性较好，支持位置和关键字参数   |
| **%** **格式化** (旧式格式化)         | `"Hello, %s" % name`                                         | 语法简单，兼容所有 Python 版本                   |



### 2. 除法

除法：左操作数除以右操作数，得到商  a/b=0.5

取整除：返回商的整数部分   a//b=0

### 3. 在Python中，没有 ++ 和 -- 

### 4. 三目运算符

``` python
表达式1 if 条件表达式 else 表达式
```

当条件表达式为True时，结果表达式1，否则结果是表达式2。

### 5. if

``` python
if 判断条件1:
判断条件1成立时执行的代码
判断条件1成立时执行的代码
...
elif 判断条件2:
判断条件1不成立,判断条件2成立时会执行的代码
判断条件1不成立,判断条件2成立时会执行的代码
...
else:
判断条件1和判断条件2都不成立,执行的代码
判断条件1和判断条件2都不成立,执行的代码
...
```

> 注意事项:
> 1. elif不要分开写，不要写成了 else if
> 2. 当判断条件1成立，判断条件2也成立时，会执行判断条件1控制的代码，不会执行判断条
> 件2执行的代码
> 3. 多分支的结构，执行也永远只会执行其中的一个分支
> 4. else后面不能再加分支了，else必须放在最后面

### 6. range函数

`range(起始值，结束值，步长) `

 起始值默认为0，步长默认为1，不包含结束值（**左闭右开**）

### 7. while / for + else

``` python
while循环或者是for循环:
循环体
else:
语句...
```

> 语法解释:
>
> 1. 只要循环不是正常退出的，就一定会执行else中的内容
> 2. 循环正常退出，是指以非break的方式跳出
> 3. 大白话：只要循环不是以break形式跳出，那么就一定会执行else中的内容

## Day3

### 1. 切片：左闭右开

### 2. 字符串常用操作方法

#### 判断类型

``` python
# 如果 string 中只包含空格，则返回True
def isspace()

# 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True
def isalnum()

# 如果 string 至少有一个字符并且所有字符都是字母则返回 True
def isalpha()

# 如果 string 只包含数字则返回 True，包含Unicode数字，，全角数字（双字节）
def isdecimal()

# 如果 string 只包含数字则返回 True，包含Unicode数字，byte数字（单字节），全角数字（双字节）
def isdigit()

# 如果 string 只包含数字则返回 True，包含Unicode 数字，全角数字（双字节），汉字数字
def isnumeric()

# 如果 string 是标题化的(每个单词的首字母大写)则返回 True
def istitle()

# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True
def islower()

# 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True
def isupper()
```

#### 查找与替换

```python
# 检查字符串是否是以 str 开头，是则返回 True
def startswith(str)

# 检查字符串是否是以 str 结束，是则返回 True
def endswith(str)

# 检测 str 是否包含在 string 中，如果start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# 与index区别,只能用位置参数，不能用keyword
def find(str,start=0,end=len(str))

# 类似于 find()，不过是从右边开始查找
def rfind(str,start=0,end=len(str))

# 跟 find() 方法类似，不过如果 str 不在 string 会报错
def index(str,start=0,end=len(str))

# 类似于 index()，不过是从右边开始
def rindex(str,start=0,end=len(str))

# 把 string 中的 old_str 替换成new_str，如果 num 指定，则替换不超过 num次
def replace(old_str, new_str, num=string.count(old))
```

#### 大小写转换

``` python
# 把字符串的第一个字符大写
def capitalize()

# 把字符串的每个单词首字母大写
def title()

# 转换 string 中所有大写字符为小写
def lower()

# 转换 string 中的小写字母为大写
def upper()

# 翻转 string 中的大小写
def swapcase()
```

#### 其他功能

``` python
# 返回一个原字符串左对齐，并使用空格填充至长度 width 的新字符串
def ljust(width)

# 返回一个原字符串右对齐，并使用空格填充至长度 width 的新字符串
def rjust(width)

# 返回一个原字符串居中，并使用空格填充至长度 width 的新字符串
def center(width)

# 截掉 string 左边（开始）的空白字符,可以去除字符 char
def lstrip(char)

# 截掉 string 右边（末尾）的空白字符，可以去除字符 char
def rstrip(char)

# 截掉 string 左右两边的空白字符，可以去除字符 char
def strip(char)

# 把字符串 string 分成一个 3 元素的元组 (str 前面, str, str 后面)
def partition(str)

# 类似于 partition() 方法，不过是从右边开始查找
def rpartition(str)

# 以 str 为分隔符拆分 string，如果num 有指定值，则仅分隔 num + 1个子字符串，str 默认包含空格
def split(str="", num)

# splitlines 只是换行，每行字符串的内容不做修改
def splitlines()

# 用字符串将可迭代对象中的元素连接起来, seq为可迭代的对象，比如','.join(['a','b','c']) -> 'a,b,c'
def join(seq)
```

### 3. 列表常用操作方法

增加: `append()`、 `extend()`、 `insert()`

删除: `del`、 `remove()`、`pop()`、 `clear()`

查询: `index()`、 `count()`、`in`、 `not in`

修改: `列表[索引] = 修改后的值`、 `reverse()`、 `sort()`

> ==index(元素值, 起始位置, 结束位置 )==: 从列表中找出某个值第一个匹配项的索引位置
>
> 注意事项：
>
> 1. 元素必须在列表中，否则会报错
> 2. 起始位置和结束位置这两个参数可以省略，默认查询整个列表

![image-20260209140542878](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209140543101.png)

### 4. 元组

**元组不可修改**

![image-20260209142907483](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209142907555.png)

### 5. 字典

**键**key是索引，必须是**不可变类型**，往往是字符串

**值**可以取任何数据类型，但**键**只能使用**字符串**、数字或元组

| 序号 | 函数                            | 描述                                                         |
| :--- | :------------------------------ | :----------------------------------------------------------- |
| 1    | `dict.clear()`                  | 删除字典内所有元素                                           |
| 2    | `dict.copy()`                   | 返回一个字典的浅复制                                         |
| 3    | `dict.fromkeys(seq, val)`       | 创建一个新字典，以序列 `seq` 中元素做字典的键，`val` 为所有键对应的初始值 |
| 4    | `dict.get(key, default)`        | 返回指定键的值，如果键不在字典中则返回 `default` 设置的默认值 |
| 5    | `key in dict`                   | 如果键在字典里返回 `True`，否则返回 `False`                  |
| 6    | `dict.items()`                  | 返回一个包含所有键值对的视图对象（可迭代）                   |
| 7    | `dict.keys()`                   | 返回一个包含所有键的视图对象（可迭代）                       |
| 8    | `dict.setdefault(key, default)` | 如果键存在则返回值，否则插入键并设置值为 `default`           |
| 9    | `dict.update(dict2)`            | 将字典 `dict2` 的键值对更新到当前字典中                      |
| 10   | `dict.values()`                 | 返回一个包含所有值的视图对象（可迭代）                       |
| 11   | `dict.pop(key)`                 | 删除并返回指定键对应的值                                     |
| 12   | `dict.popitem()`                | 删除并返回字典中的一个键值对（在 Python 3.7+ 中为后进先出）  |

> default 默认为 None

**字典的特征：**

**可变容器**：字典中的数据是可变的，和列表一样，是可变容器，而元组是不可变容

器

**键的唯一性**：字典中的键必须是唯一的，如果同一个键被赋值多次，那么后面的值

会把前面的值覆盖

**键的类型限制**：字典使用哈希表存储，字典的键必须是可哈希的，也就是必须是不

可变类型，一般建议设置为字符串类型



### 6. 除了变量名，函数名也可以被del()删除

### 7. 集合

> 集合主要是用来去重。
>
> 集合的定义
>
> - 创建空集合 `my_set = set()`
>
> - 创建有元素的集合 `my_set = {元素1, 元素2, 元素3 ...}`
>
> - 通过序列创建集合(这一步会去重) `my_set = set(序列名)`

| 编号 | 方法                            | 描述                                           |
| :--- | :------------------------------ | :--------------------------------------------- |
| 1    | `add()`                         | 为集合添加元素                                 |
| 2    | `clear()`                       | 移除集合中的所有元素                           |
| 3    | `copy()`                        | 拷贝一个集合                                   |
| 4    | `difference()`                  | 返回多个集合的差集                             |
| 5    | `difference_update()`           | 移除集合中那些同时存在于指定集合中的元素       |
| 6    | `discard()`                     | 删除集合中指定的元素（如果元素不存在，不报错） |
| 7    | `intersection()`                | 返回集合的交集                                 |
| 8    | `intersection_update()`         | 用交集更新原集合                               |
| 9    | `isdisjoint()`                  | 判断两个集合是否没有交集，无则返回 `True`      |
| 10   | `issuperset()`                  | 判断当前集合是否为另一个集合的超集             |
| 11   | `pop()`                         | 随机移除并返回一个元素                         |
| 12   | `remove()`                      | 移除指定元素（若不存在则报错）                 |
| 13   | `symmetric_difference()`        | 返回两个集合的对称差集                         |
| 14   | `symmetric_difference_update()` | 用对称差集更新原集合                           |
| 15   | `union()`                       | 返回两个集合的并集                             |
| 16   | `update()`                      | 用并集更新原集合                               |
| 17   | `len()`                         | 计算集合元素个数（内置函数，非集合方法）       |

> 集合还支持特定的运算符来求交集、并集和差集
>
> - &：交集
>
> - -：差集
>
> - |：并集

```python
# 求交集、并集和差集
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# 并集
union_set = set1 | set2
print(union_set) # 输出: {1, 2, 3, 4, 5, 6}

# 差集
diff_set = set1 - set2
print(diff_set) # 输出: {1, 2}

# 交集
inter_set = set1 & set2
print(inter_set) # 输出: {3, 4}
```

### 8. 公共运算符

| 运算符             | 描述                       | 支持的容器类型                 |
| :----------------- | :------------------------- | :----------------------------- |
| `+`                | 合并                       | 字符串、列表、元组             |
| `*`                | 复制                       | 字符串、列表、元组             |
| `in`               | 元素是否存在（字典是键）   | 字符串、列表、元组、字典、集合 |
| `not in`           | 元素是否不存在（字典是键） | 字符串、列表、元组、字典、集合 |
| `[start:end:step]` | 切片（对序列进行截取）     | 字符串、列表、元组             |

| 容器类型    | `==` / `!=`（相等 / 不等）       | `>` / `<` / `>=` / `<=`（大小比较）  |
| :---------- | :------------------------------- | :----------------------------------- |
| 列表 / 元组 | 比较元素、顺序、数量是否完全相同 | 按元素顺序逐个比较，短的前缀容器更小 |
| 集合        | 比较元素是否相同（顺序无关）     | 判断子集/超集关系（一般少用）        |
| 字典        | 比较键值对是否相同（顺序无关）   | **不支持**，会抛出 `TypeError`       |

### 9. 公共方法

| 编号 | 函数          | 字符串 (str) | 列表 (list) | 元组 (tuple) | 字典 (dict) | 集合 (set) | 描述与说明                                                   |
| ---- | ------------- | ------------ | ----------- | ------------ | ----------- | ---------- | ------------------------------------------------------------ |
| 0    | `del`         | ×            | ✓           | ×            | ✓           | ×          | **删除容器中的元素**：从列表、字典等可变容器中移除指定的元素或键值对。 |
| 1    | `len()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取长度**。返回容器中元素的数量。                         |
| 2    | `max()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取最大值**。返回容器中“最大”的元素。                     |
| 3    | `min()`       | ✓            | ✓           | ✓            | ✓           | ✓          | **获取最小值**。返回容器中“最小”的元素。                     |
| 4    | `sum()`       | ×            | ✓           | ✓            | ×           | ✓          | **求和**。返回容器中所有元素的总和（元素必须是数字类型）。   |
| 5    | `sorted()`    | ✓            | ✓           | ✓            | ✓           | ✓          | **排序**。返回一个新的已排序的列表，不改变原容器。           |
| 6    | `reversed()`  | ✓            | ✓           | ✓            | ✓           | ×          | **反转**。返回一个反转==迭代器==。（想打印迭代器只能通过遍历或使用该迭代器创建一个list用于打印） |
| 7    | `enumerate()` | ✓            | ✓           | ✓            | ✓           | ✓          | **枚举**。返回一个枚举对象，包含索引和值。                   |

``` python
word_list = ['hello', 'today', 'good', 'day']
for index, word in enumerate(word_list):
    print(index, word)
```

运行结果：

![image-20260209164702501](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209164702561.png)

```python
word_list =['hello','today','good','day']
word_dict = {}
for index，word in enumerate(word_list): # 遍历可选代对象时，每个位置依次给与编号
    word_dict[word]= index
print(word_dict)
```

运行结果：

![image-20260209164836876](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260209164836925.png)

### 10. 推导式

基本语法：

- if 的情况：==[表达式 for 项目 in 可迭代对象 if 条件]==

- if-else的情况==[表达式 if 条件 else 表达式 for 项目 in 可迭代对象 ]==

**常见的推导式类型**

| 推导式类型 | 语法结构                                                   | 描述                           |
| ---------- | ---------------------------------------------------------- | ------------------------------ |
| 列表推导式 | `[expr for item in iterable if condition]`                 | 创建一个新的列表。             |
| 字典推导式 | `{key_expr: value_expr for item in iterable if condition}` | 创建一个新的字典。             |
| 集合推导式 | `{expr for item in iterable if condition}`                 | 创建一个新的集合（自动去重）。 |

## Day4

### 1. 全局变量

如果在函数内要修改全局变量的值，需要使用global关键字声明

不声明直接赋值则会重新创建一个同名局部变量

```python
a = 100

def testA():
	print(a)
    
def testB():
    # global 关键字声明a是全局变量
    # 如果这里没有写global a, 那么 a = 200就相当于是在testB中重新定义了一个局部变量
    global a
    a = 200
    print(a)
    
testA() # 100
testB() # 200
print(f'全局变量a = {a}') # 全局变量a = 200
```

### 2. 函数可以作为 (另一个函数的)参数进行传递

```python
# 定义加法函数
def get_sum(a, b):
	return a + b

# 定义减法函数
def get_substract(a, b):
	return a - b

# 定义计算函数
def calculate(a, b, fn):
    """
    自定义函数, 模拟计算器, 传入什么 函数(对象), 就做什么操作.
    :param a: 要操作的第1个整数
    :param b: 要操作的第2个整数
    :param fn: 具体的操作规则
    :return: 计算结果.
    """
    return fn(a, b)

# 把函数作为calculate的参数进行传递（传递行为）
print(calculate(10, 20, get_sum))
print(calculate(10, 20, get_substract))
```

> 此时被传递函数不加括号，加括号则传递的是函数返回值

### 3. 函数返回值，拆包

可以返回多个结果，默认是元组类型

return返回多个值的时候，单个值的类型没有限制，可以是列表、元组、字典等等

```python
def return_num():
	return 1,2

result = return_num()
print(result) # (1,2)
print(type(result)) # <class 'tuple'>
```

也可以用多个变量接收多个返回值(变量个数必须和返回值个数相同)

```python
def return_num():
	return 1,2

a,b=return_num() # 对元组拆包
print(a) # 1
print(b) # 2
```

**对元组、列表或者字典都可以进行拆包操作**

```python
# 对列表拆包
my_list = [1,3.14,'Cskaoyan',True]
num,pi,name,my_bool=my_list
print(f"num:{my_list}, pi:{pi}, name:{name}, my_bool:{my_bool}")

# 对字典拆包
dict1 = {'name':'李云龙','age':20,'gender':'男'}

# 对字典拆包的时候，获取到的是key值
key1,key2,key3 = dict1
print(f"key1:{key1},key2:{key2},key3:{key3}")
```

### 4. 函数的多种参数

### 5. 引用

**python****中的引用？**

**变量** **≠** **对象**：变量只是 “引用的名字”，对象才是真正的数据；

比如 a = 10：

10 是**整数对象**（存在内存里）

a 是**引用**（指向 10 这个对象的 “地址”）

再比如 b = a：

不是把 10 复制一份给 b，而是让 b 也指向 10 这个对象（两个引用指向同一个对象）。

![image-20260210143806038](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260210143806155.png)

**补充说明**：局部变量的引用在栈帧中，全局变量的引用在模块的命名空间（堆）中。

每次函数调用，CPython（解释器） 会创建一个 PyFrameObject ：

```python
栈帧（frame）：
- 局部变量表（fast locals）
- 操作数栈
- 指令指针
```

> 这个“栈帧”是 **虚拟机层面的栈**，不是 C 语言意义上的 CPU 栈。

**验证引用传递**

打印a和b的地址值，可以看到地址值是一样的，实际是同一个数据，并不是内存中的两份数据

```python
def fuc1():
    a = 10
    b = a
    
    print(id(a)) # 140730885489864
    print(id(b)) # 140730885489864
    
if __name__ == '__main__':
	fuc1()
```

> **结论：**Python中只有引用传递。一句话：**一切皆引用**
>
> 函数传参时，**传递的是 “指向堆中对象的引用”**，不是对象本身；
>
> 引用的存储位置会变（比如参数引用存到新栈帧），但堆中对象的位置不变；
>
> 最终效果由 “对象是否可变” 决定，核心是 “改引用” 还是 “改堆中对象”。

**可变类型：列表、字典、集合**——修改对中的内容，所有对其的引用都变

**不可变类型：整数、字符串、元组**——无法在函数内修改函数外某个变量的值（不考虑全局变量）

> 1 引用是 **“地址”**：变量存的是引用（指向堆中对象），不是对象本身；
>
> 2 **存储分工**：
>
> - 堆：存所有对象（真正的数据）
>
> - 栈帧：存函数内局部变量 / 参数的引用（函数结束销毁）
>
> - 全局引用：存模块命名空间（长期存在）
>
> 3 **传参本质**：只传引用（引用从外部到函数栈帧），不改堆中对象地址
>
> 4 **效果判断**：
>
> - **不可变对象：改栈帧里的引用** **→** **外部不变**
>
> - **可变对象：改堆中的对象内容** **→** **外部也变（因为两个引用指向同一块堆空间）**

### 6. copy()

使用copy对可变对象进行赋值，会将原对象的值复制给另一个堆空间，新的可变对象引用指向此空间，从而两个引用指向不同的空间，不会同步改变

```python
list = [10, 20]
list1 = list # list1的引用指向list引用的堆空间，list和list1的id相同

list = [10, 20]
list1 = list.copy() # 将list的值赋给list1，list和list1的id不同
```

### 7. 匿名函数

格式：==lambda 参数1, 参数2, ... : 表达式 	# 冒号前是参数，冒号后是返回结果的表达式==

```python
"""
普通函数
"""
def get_sum(a, b):
	return a + b # 求和

def get_sub(a, b):
	return a - b # 差

def get_mul(a, b):
	return a * b # 积
# ...

"""
匿名函数
"""
def cal_num(a,b,fn):
	return fn(a,b)

a = 10
b = 20
# 求和
sum_result = cal_num(a,b,lambda a,b:a+b)
sub_result = cal_num(a,b,lambda a,b:a-b)
mul_result = cal_num(a,b,lambda a,b:a*b)
```

