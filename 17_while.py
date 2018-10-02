'''
7.2 while循环简介练习
'''

'''
7-4 披萨吧、配料
'''
prompt = "\nPlease enter pizza toppings： "
prompt += "\n(Enter 'quit' when you are finished.)"
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message + " will be added to the pizza.")
'''
7-5 电影票
'''
active = True
p = "\n请输入你的年龄："
p += "\n(输入大于200则结束)"
while active:
    age = input(p)
    age = int(age)
    if age < 3:
        print("您可免费观看电影 ！")
    elif age >= 3 and age <= 12:
        print("您的票价为： 10 美元")
    elif age > 12 and age <= 200:
        print("您的票价为： 15 美元")
    elif age > 200:
        active = False
'''
7-6 三个出口
'''

#  用条件测试来结束循环 即7-4

# 7-4 变种，用变量active来控制结束循环的时机
prompt = "\n请输入披萨配料： "
prompt += "\n(输入'quit'结束)"

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print("我们会在披萨里添加" + message)

# 7-4 变种，用break语句在用户输入'quit'时结束循环
p = "\n 请输入配料表"
p += "\n(输入'quit'结束）"
message = ""
while message != 'quit':
    message = input(p)
    if message == 'quit':
        break
    else:
        print("我们将会在披萨中添加" + message)


'''
7-7无限循环
'''

name = "Don"
while name != "SB":
    print("Don 是天才。")