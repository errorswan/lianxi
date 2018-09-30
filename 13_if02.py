'''
5.4 if处理列表练习
'''

'''
5-8 以特殊方式跟管理员打招呼
'''

name = ['admin', 'don', 'errorswan', 'xiaoxiao', 'sb']
for n in name:
    if n == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + n + ", thank you for logging in again.")

'''
5-9 处理没有用户的情景
'''

name = []
if name:
    for n in name:
        if n == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + n + ", thank you for logging in again.")
else:
    print("\nWe need to find some users!")

'''
5-10 检查用户名
'''

current_users = ['admin', 'don', 'errorswan', 'xiaoxiao', 'sb']
new_users = ['david', 'lisa', 'SB', 'don', 'errorswan']

for new_user in new_users:
    new_user = new_user.lower()
    if new_user in current_users:
        print(new_user + " has been used. ""You need log in another users.")
    else:
        print(new_user + " can be used.")

'''
5-11 序数
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numeber in numbers:
    if numeber == 1:
        print("1st")
    elif numeber == 2:
        print("2nd")
    elif numeber == 3:
        print("3rd")
    else:
        print(str(numeber) + "th")