'''9-12 多个模块'''

from User_27_1 import User

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