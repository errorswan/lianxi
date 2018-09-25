'''
3.2 修改添加和删除元素练习
'''

'''
3-4 嘉宾名单
'''
dinner = ['mom', 'dad', 'granddad']
for invite in dinner:
    print("I will invite " + invite + " to take dinner with me!")


'''
3-5 修改嘉宾名单,一位嘉宾无法赴约，邀请另一位
'''
dinner = ['mom', 'dad', 'granddad']
not_come = dinner.pop(0)
print(not_come.title() + " will not come today.")# 第一位嘉宾没法赴约

dinner.insert(0, 'xiaoxiao')# 增加新邀请人
for invite in dinner:
    print("I will invite " + invite + " to take dinner with me!")


'''
3-6添加嘉宾,添加三位嘉宾
'''
print("I find a bigger desk right now")
dinner.insert(0,'mom')# 嘉宾加到列表首位
dinner.insert(3,'don')# 加到列表中间
dinner.append('sister')# 加到列表末尾
for invite in dinner:
    print("I will invite " + invite + " to take dinner with me!")


'''
3-7缩减名单，只能邀请两位
'''

#print(dinner)
# 打印你只能邀请两位嘉宾的消息
print('Sorry everyone,I can only invite two guests to take dinner since the table has not arrived.')

# 使用pop()删除，直到剩余俩位，每弹出一条都打出一条消息说明你的抱歉
sorry = dinner.pop(1)
print("Sorry " + sorry + ", I cann't invite you to take dinner")
sorry01 = dinner.pop(1)
print("Sorry " + sorry01 + ", I cann't invite you to take dinner")
sorry02 = dinner.pop(1)
print("Sorry " + sorry02 + ", I cann't invite you to take dinner")
sorry03 = dinner.pop(1)
print("Sorry " + sorry03 + ", I cann't invite you to take dinner")

# 告诉余下两位，都在受邀之列
# print(dinner)
print(dinner[0].title() + " , you are still invited to take dinner.")
print(dinner[1].title() + " , you are still invited to take dinner.")

# 用del删除最后两位,并打印该名单
del dinner[0]
del dinner[0]
print(dinner)