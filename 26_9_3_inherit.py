"""9.3继承练习"""

'''9-6冰淇淋小店'''


class IceCreamStand():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Lemon']

    def describe_restaurant(self):
        """描述餐馆信息"""
        message = self.restaurant_name + ' ' + self.cuisine_type
        return  message.title()

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("The restraurant is openning.")

    def show_flavors(self):
        print(self.flavors)

my_IceCreamStand = IceCreamStand('Don', 'dessert')
my_IceCreamStand.show_flavors()

'''9-7 管理员'''

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

class Admin(User):

    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)

        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for self.privilege in self.privileges:
            print("Admin " + self.privilege + ".")

my_admin = Admin('don', 'hu', 28)
my_admin.show_privileges()

'''9-8 权限'''


class Privileges():

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for self.privilege in self.privileges:
            print("Admin " + self.privilege + ".")

class Admin(User):

    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges() # 将类Privileges赋值到属性privilege中

m_admin = Admin('don', 'hu',28)
m_admin.privileges.show_privileges()

'''9-9 电瓶升级'''

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery(): # 定义一个名为Battery的新类
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """表示汽车的各个方面，具体到电动汽车，"""

    def __init__(self, make, model, year):
        """
       电动车的独特之处
       初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tsl = ElectricCar('byd', 'song', 2018 )
my_tsl.battery.get_range()
my_tsl.battery.upgrade_battery()
my_tsl.battery.get_range()