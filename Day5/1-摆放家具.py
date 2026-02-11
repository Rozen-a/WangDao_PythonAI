"""
练习摆放家具案例
"""
class HouseItem:
    """
    家具类
    """

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具：{self.name} 占地 {self.area} 平米'


class House:
    """
    房子类
    """

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return (f'--------房子信息--------\n'
                f'户型：{self.house_type}\n'
                f'总面积：{self.area}\n'
                f'剩余面积：{self.free_area}\n'
                f'家具：{self.item_list}\n')

    def add_item(self, item:HouseItem):
        if item.area<=self.free_area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        print(f'已成功添加家具"{item.name}", 剩余面积：{self.free_area}')

if __name__ == '__main__':
    # 创建家具
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)

    # 创建房子
    my_house = House('两室一厅', 70)

    # 添加家具
    my_house.add_item(bed)
    my_house.add_item(chest)
    my_house.add_item(table)

    print()

    # 查看房子信息
    print(my_house)