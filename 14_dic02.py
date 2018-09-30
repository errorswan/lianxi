'''
6.3 遍历字典练习
'''

'''
6-4 词汇表 2
'''

vocabulary = {'列表': '由一系列按特定顺序排列的元素组成。',
              'for循环': '对列表中的每个元素都执行相同的操作。',
              'if语句': '条件测试语句。',
              '字典': '一系列键-值对。',
              '切片': '处理列表的部分元素。',
              '变量': '储存一个与变量相关信息的值',
              '字符串': '就是一系列字符,用引号括起的都是字符串',
              '元组': '不能修改的值称为不可变的，而不可变的列表 称为元组',
              '条件测试': '一个值为True或False的表达式称为条件测试',
              '浮点数': '将带小数点的数字都称为浮点数'}

for key,value in vocabulary.items():
    print(key + ":" + value)

'''
6-5 河流
'''

rivers = {'nile': 'egypt', 'changjiang': 'china', 'amazon': 'brazil'}

for key,value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")

for river in rivers.keys(): # 打印河流
    print("The " + river.title())

for country in rivers.values(): # 打印国家
    print(country.title())

'''
6-6 调查
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

crew = ['don', 'xiaoxiao', 'jen', 'sarah', 'phil']
for men in crew:
    if men in favorite_languages.keys():
        print(men.title() + ", thank you for taking the poll.")
    else:
        print(men.title() + ", you are invited to investigate.")

'''for men in favorite_languages.keys():
    if men in crew:
        print(men.title() + ", thank you for taking the poll.")
    else:
        print(men.title() + ", you are invited to investigate.")
'''