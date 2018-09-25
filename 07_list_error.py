'''
3-11 有意引发错误
'''
dinner = ['mom', 'xiaoxiao', 'dad', 'don', 'granddad', 'sister']
 #print(dinner[6])# 6 超出列表范围

print(dinner[-1])# 正确检索最后元素

dinner = []
#print(dinner[-1]) # 列表为空，无法检索最后元素

dinner = ['mom', 'xiaoxiao', 'dad', 'don', 'granddad', 'sister']
print(dinner)
list_number = len(dinner)
print(str(list_number))