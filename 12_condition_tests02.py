'''
5-2 更多的条件测试
'''

# 检查两个字符串相等或不等
fruite = "apple"
print("Is fruite == 'apple'? I predict True.")
print(fruite == 'apple')

print("\nIs fruite == 'banana'? I predict False.")
print(fruite == 'banana')

# 使用函数lower（）测试
print("\nIs fruite == 'apple'? I predict True.")
print(fruite == 'Apple')

print("\nIs fruite == 'apple'? I predict True.")
f = 'Apple'
print(fruite == f.lower())

#检查两个数相等、不等、大于、小于、大于等于、小于等于
n1 = 1
n2 = 2
print("\nn1 = n2")
print(n1 == n2)

print("n1 != n2")
print(n1 != n2)

print("n1 > n2")
print(n1 > n2)

print("n1 < n2")
print(n1 < n2)

print("n1 >= n2")
print(n1 >= n2)

print("n1 <= n2")
print(n1 <= n2)

# 使用关键字and和or测试

print("\nn1 > 2 and n1 >1")
print(n1 > 2 and n1 >1)

print("n1 <2 or n1 <1")
print(n1 <2 or n1 <1)

# 检查特定值是否包含在列表中
number = [1, 2, 3, 4, 5, 6]
print("\nIs 2 in number? I predict True")
print(2 in number)

print("Is 27 not in number? I predict True")
print(27 not in number)