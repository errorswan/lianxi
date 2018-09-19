'''\
2.3个性化信息
'''
name = "Eric"
print("Hello Eric,would you like to learn some Python today?")

'''
2.4调整名字的大小写
'''
name = "don hu"
# 首字母大写显示人名
print(name.title())
# 大写显示人名
print(name.upper())
# 小写显示人名
print(name.lower())

'''
2.4名言
'''
print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')

'''
2.6 名言2
'''
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(famous_person + " once said," + message)

'''
2.7 剔除人名中的空白
'''
name = " Don Hu "
# 使用\t,\n
print("Don\nHu")
print("Don\tHu")
print("Don\n\tHu")
# 人名处理
print(name+"lalala")
# 去除前端空格
print(name.lstrip() + "lalala")
# 去除末端空格
print(name.rstrip() + "lalala")
# 去除前后空格
print(name.strip() + "lalala")
