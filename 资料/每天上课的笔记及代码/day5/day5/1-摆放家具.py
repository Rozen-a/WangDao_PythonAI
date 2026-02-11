# 作者: 王道 龙哥
# 2026年02月11日09时26分54秒
# xxx@qq.com


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name} 占地 {self.area} 平米'


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 一开始空余面积等于房子面积
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return "户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s" % (self.house_type, self.area,
                                                             self.free_area, self.item_list)

    def add_item(self, item: HouseItem):
        """
        :HouseItem 这是注解，是为了编程时能够联想的作用
        :param item:
        :return:
        """
        if self.free_area >= item.area:  # 如果剩余面积大于家具面积
            self.item_list.append(item.name)
            self.free_area -= item.area
            print(f'添加{item.name}家具成功')
        else:
            print('房子没有空间了')


if __name__ == '__main__':
    # 1. 创建家具
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)

    print(bed)
    print(chest)
    print(table)

    # 2. 创建房子对象
    my_home = House("两室一厅", 60)
    print('-' * 50)
    print(my_home)
    my_home.add_item(bed)
    print('-' * 50)
    print(my_home)
