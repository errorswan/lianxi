'''
5.3 语句练习
'''

'''
5-3 外星人颜色 #1
'''

alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You got 5 points.")

if 'yellow' in alien_color:
    print("You got 5 points.")

if 'blue' in alien_color:
    print("You got 5 points.")


'''
5-4 外星人颜色 #2
'''
alien_color = ['green', 'yellow', 'red']
color = 'green'
if color == 'green':
    print("\nYou got 5 points.")
else:
    print("You got 10 points.")

if color != 'green':
    print("You got 10 points.")
else:
    print("You got 5 points.")

'''
5-5 外星人颜色 #3
'''
alien_color = ['green', 'yellow', 'red']
color = 'red'
if color == 'green':
    print("\nYou got 5 points.")
elif color == 'yellow':
    print("\nYou got 10 points.")
elif color == 'red':
    print("\nYou got 15 points.")

color = 'yellow'
if color == 'green':
    print("\nYou got 5 points.")
elif color == 'yellow':
    print("\nYou got 10 points.")
elif color == 'red':
    print("\nYou got 15 points.")

color = 'green'
if color == 'green':
    print("\nYou got 5 points.")
elif color == 'yellow':
    print("\nYou got 10 points.")
elif color == 'red':
    print("\nYou got 15 points.")

'''
5-6 人生的不同阶段
'''

age = 28

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are learnning walking.")
elif age >=4 and age < 13:
    print("You are a child.")
elif age >=13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age <65:
    print("You are a adult")
elif age >= 65:
    print("You are a old man.")

'''
5-7 喜欢的水果
'''
favorite_fruits = ['apple', 'pitch', 'banana']
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'pitch' in favorite_fruits:
    print("You really like pitchs!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'pear' in favorite_fruits:
    print("You really like pears!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
