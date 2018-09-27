'''
4.4切片练习
'''

'''
4-10 切片
'''
# 列表前三元素
pizzas = ['new york', 'chicago', 'california', 'pan', 'thick']
list = pizzas[:3]
print("The first three items in the list are:")
print(list)

# 列表中间三元素
pizzas = ['new york', 'chicago', 'california', 'pan', 'thick']
list = pizzas[1:4]
print("Three items from the middle of the list are:")
print(list)

# 列表末尾三元素
pizzas = ['new york', 'chicago', 'california', 'pan', 'thick']
list = pizzas[2:]
print("The last three items in the list are:")
print(list)

'''
4-11你的比萨和我的比萨
'''
pizzas = ['new york', 'chicago', 'california', 'pan', 'thick']
friend_pizzas = pizzas[:]

pizzas.append('kfc')
friend_pizzas.append('mac download')

print("My favorite pizzas are:")
for p in pizzas:
    print(p)
print("My friend's favorite pizzas are:")
for m in friend_pizzas:
    print(m)

'''
4-12
'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for m in my_foods:
    print(m)

print("\nMy friend's favorite foods are:")
for f in friend_foods:
    print(f)