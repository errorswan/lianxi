'''
4.3 列表数值练习
'''

'''
4-3 数列20
'''
for number in range(1,21):
    print(number)

'''
4-4 一百万
'''
number02 = [n for n in range(1,1000001)]
print(number02)

'''
4-5 计算1~1000000的总和
'''
number = list(range(1,1000001))
print(min(number))
print(max(number))
print(sum(number))

'''
4-6 奇数
'''

ji = list(range(1,21,2))
for jishu in ji:
    print(jishu)

'''
4-7 3的倍数
'''

chu3 = list(range(3,31,3))
for yin in chu3:
    print(yin)

'''
4-8 立方
'''
# 此处为正常
lifang = []
for value in range(1,11):
    lifang.append(value**3)# 创建列表
for i in lifang:
    print(i)# 打印数值

# 此处为立方解析
lifang = [value**3 for value in range(1,11)]
for yin in lifang:
    print(yin)

'''
4-9 立方解析
'''

lifang = [value**3 for value in range(1,11)]
print(lifang)