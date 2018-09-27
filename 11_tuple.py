'''
4.5 元组练习
'''

'''
4-13 自助餐
'''

# 打印元组
foods = ('apple', 'cake', 'pork', 'beaf', 'tea')
for food in foods:
    print(food)

# 尝试修改内容
foods = ('apple', 'cake', 'pork', 'beaf', 'tea')
foods.append('coke')
print(foods)

# 用赋值替代两种食物
foods = ('apple', 'cake', 'pork', 'beaf', 'tea')
foods = ('apple', 'coke', 'pear', 'beaf', 'tea')
for food in foods:
    print(food)