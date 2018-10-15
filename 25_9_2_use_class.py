"""9.2使用类和实例练习"""

'''9-4 就餐人数'''
class Restaurant():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆信息"""
        message = self.restaurant_name + ' ' + self.cuisine_type
        return  message.title()

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("The restraurant is openning.")

    def read_number(self):
        """打印用餐人数"""
        print("There is " + str(self.number_served) +
              " people have dinner in this restaurant.")

dinner = Restaurant('starbucks', 'coffee')
print(dinner.describe_restaurant())
dinner.open_restraurant()
dinner.read_number()

''''''

class Restaurant():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆信息"""
        message = self.restaurant_name + ' ' + self.cuisine_type
        return  message.title()

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("The restraurant is openning.")

    def read_number(self):
        """打印用餐人数"""
        print("There is " + str(self.number_served) +
              " people have dinner in this restaurant.")

    def set_number_served(self, people):
        """设置就餐人数"""
        self.number_served = people

dinner = Restaurant('starbucks', 'coffee')
print(dinner.describe_restaurant())
dinner.open_restraurant()

dinner.set_number_served(1000)
dinner.read_number()

''''''

class Restaurant():
    """创建餐馆的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆信息"""
        message = self.restaurant_name + ' ' + self.cuisine_type
        return  message.title()

    def open_restraurant(self):
        """餐馆的营业状态"""
        print("The restraurant is openning.")

    def read_number(self):
        """打印用餐人数"""
        print("There is " + str(self.number_served) +
              " people have dinner in this restaurant.")

    def set_number_served(self, people):
        """设置就餐人数"""
        self.number_served = people

    def increment_number_served(self,person):
         """将人数增加指定的量"""
         self.number_served += person

dinner = Restaurant('starbucks', 'coffee')
print(dinner.describe_restaurant())
dinner.open_restraurant()

dinner.set_number_served(1000)
dinner.read_number()

dinner.increment_number_served(100)
dinner.read_number()

'''9-5 尝试登录次数'''

class User():
    """用户属性"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """返回简洁的用户信息"""
        full_name = str(self.age) + ' ' + self.first_name + ' ' + self.last_name
        return full_name.title()

    def greet_user(self):
        """问候信息"""
        print("How is everting today!")

    def increment_login_attempts(self):
        """登录次数增加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """登录次数重置为0"""
        self.login_attempts = 0

don = User('don', 'hu', 28)
print(don.describe_user())

don.increment_login_attempts()
print(str(don.login_attempts))

don.increment_login_attempts()
print(str(don.login_attempts))

don.increment_login_attempts()
print(str(don.login_attempts))

don.reset_login_attempts()
print(str(don.login_attempts))