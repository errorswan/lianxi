"""9.1 创建和使用类练习"""

'''9-1 餐馆'''

class Restaurant():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐馆信息"""
        print("餐馆的名称是： " + self.restaurant_name.title())
        print("餐馆的类型是： " + self.cuisine_type)

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("餐馆正在营业")
'''实例'''

class Restaurant():
    --snip--

my_restaurant = Restaurant('深夜食堂', fry)
print("\nMy restaurant's name is " + my_restaurant.restaurant_name.title() + ".")
print("My restaurant's cuisine type is " + my_restaurant.cuisine_type + ".")

my_restaurant.describe_restaurant()
my_restaurant.open_restraurant()

'''9-2 三家餐馆'''

class Restaurant():
    --snip--

don_restaurant = Restaurant('Starbucks', coffee)
print("\nMy restaurant's name is " + don_restaurant.restaurant_name.title() + ".")
print("My restaurant's cuisine type is " + don_restaurant.cuisine_type + ".")
don_restaurant.describe_restaurant()

a_restaurant = Restaurant('一点点', milktea)
print("\nMy restaurant's name is " + a_restaurant.restaurant_name.title() + ".")
print("My restaurant's cuisine type is " + a_restaurant.cuisine_type + ".")
a_restaurant.describe_restaurant()

b_restaurant = Restaurant('kaoyu', toast)
print("\nMy restaurant's name is " + b_restaurant.restaurant_name.title() + ".")
print("My restaurant's cuisine type is " + b_restaurant.cuisine_type + ".")
b_restaurant.describe_restaurant()


'''9-3 用户'''

class User():
    """用户属性"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("name:" + self.first_name.title() + " " + self.last_name.title())
        print("age:" + str(self.age))

    def greet_user(self):
        print("How is everting today!")


my_name = User('don', 'hu', 28)
your_name = User('xiaoxiao', 'shu', 24)

my_name.describe_user()
my_name.greet_user()

your_name.describe_user()
your_name.greet_user()