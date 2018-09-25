'''
3.3 组织列表练习
'''

'''
3-8 放眼世界
'''
travel = ['Japan', 'USA', 'England', 'France', 'Thailand', 'Norway']
print(travel)# 原始列表

print(sorted(travel))# 暂时改变,按字母顺序排序

print(travel)# 核实未变

print(sorted(travel,reverse=True))# 按字母相反顺序排列

print(travel)# 核实未变

travel.reverse()
print(travel)# 修改排列顺序

travel.reverse()
print(travel)# 恢复排列顺序

travel.sort()
print(travel)# 永久改变排序，按字母

travel.sort(reverse=True)
print(travel)# 字母反顺序


'''
3-9 晚餐邀请
'''
dinner = ['mom', 'xiaoxiao', 'dad', 'don', 'granddad', 'sister']
number = len(dinner)
print("I have invited " + str(number) + " person to take dinner.")

'''
3-10 尝试使用各个函数
'''
fruit = ['apple', 'pear', 'banana',  'pitch', 'grape']

fruit.sort()
print(fruit) # 永久按字母顺序排序

fruit.sort(reverse=True)
print(fruit) # 按字母反向排序

fruit = ['apple', 'pear', 'banana',  'pitch', 'grape']
print(sorted(fruit))
print(fruit)# 临时改变排序，并验证

print(sorted(fruit,reverse=True))
print(fruit)# 临时反字母顺序排，并验证

number = len(fruit)
print(str(number))
