'''9-11 导入Admin 类'''

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
        self.privileges = Privileges()