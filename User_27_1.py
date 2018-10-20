'''9-12 多个模块'''

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