'''9-12 多个模块'''

from User_27_1 import User
from my_AP_27_1 import Admin, Privileges

my_Admin = Admin('don', 'hu', 28)
my_Admin.privileges.show_privileges()