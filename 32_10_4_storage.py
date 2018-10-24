"""10.4 存储数据练习"""

'''10-11 喜欢的数字'''
import json

favor_num = input("What is your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favor_num, f_obj)


filename = 'favorite_number.json'
try:
    with open(filename) as f_obj:
        favor_num = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    print("I know your favorite number! It's " + favor_num + ".")

'''10-12 记住喜欢的数字'''

import json

def get_stored_number():
    """如果存储了数字就获取它"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favor_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favor_num

def get_new_number():
    """提示用户输入新的数字"""
    favor_num = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(favor_num, f_obj)

def show_number():
    """指出数字"""
    favor_num = get_stored_number()
    if favor_num:
        print("I know your favorite number! It's " + favor_num + ".")
    else:
        favor_num = get_stored_number()
        print("I will know your favorite number! It's " + favor_num + ".")

show_number()

'''10-13 验证用户'''

import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            usrname = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usrname

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(filename, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    print("Is " + username + " your username?")
    newuser = input("(y/n)")
    if newuser == 'y':
        print("Welcome back, " + username + "!")
    elif newuser == 'n':
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()

