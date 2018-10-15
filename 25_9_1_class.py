"""9.1 创建和使用类练习"""

'''9-1 餐馆'''

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
'''实例'''

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

my_restaurant = Restaurant('深夜食堂', 'fry')
print(my_restaurant.describe_restaurant())
my_restaurant.open_restraurant()

'''9-2 三家餐馆'''

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

don_restaurant = Restaurant('Starbucks', 'coffee')
print(don_restaurant.describe_restaurant())
don_restaurant.open_restraurant()

a_restaurant = Restaurant('一点点', 'milktea')
print(a_restaurant.describe_restaurant())
a_restaurant.open_restraurant()

b_restaurant = Restaurant('kaoyu', 'toast')
print(b_restaurant.describe_restaurant())
b_restaurant.open_restraurant()


'''9-3 用户'''

class User():
    """用户属性"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """返回简洁的名字信息"""
        full_name = str(self.age) + ' ' + self.first_name + ' ' + self.last_name
        return full_name.title()

    def greet_user(self):
        """问候信息"""
        print("How is everting today!")


my_name = User('don', 'hu', 28)
print(my_name.describe_user())
my_name.greet_user()

your_name = User('xiaoxiao', 'shu', 24)
print(your_name.describe_user())
your_name.greet_user()


