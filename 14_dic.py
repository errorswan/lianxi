'''
6.2 使用字典练习
'''

'''
6-1 人
'''

message = {'first_name': 'Don', 'last_name': 'Hu', 'age': 28, 'city': 'YongKang'}
print(message['first_name'])
print(message['last_name'])
print(message['age'])
print(message['city'])

'''
6-2 喜欢的数字
'''
lucky_num = {'Don': 7, 'Xiaoxiao': 8, 'Li': 5, 'Fu': 3, 'Yao': 9}
print(lucky_num)

'''
6-3 词汇表
'''
vocabulary = {'列表': '由一系列按特定顺序排列的元素组成。',
              'for循环': '对列表中的每个元素都执行相同的操作。',
              'if语句': '条件测试语句。',
              '字典': '一系列键-值对。',
              '切片': '处理列表的部分元素。'}
print("列表：" + vocabulary['列表'])
print("for循环：" + vocabulary['for循环'])
print("if语句：" + vocabulary['if语句'])
print("字典：" + vocabulary['字典'])
print("切片：" + vocabulary['切片'])
