'''9-10 导入Restaurant 类'''

class Restaurant():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆信息"""
        message = self.restaurant_name + ' ' + self.cuisine_type
        return  message.title()

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("The restraurant is openning.")