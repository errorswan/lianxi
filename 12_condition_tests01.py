'''
5.2 条件测试练习
'''

'''
5-1 条件测试
'''

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs car == 'subaru'? Case insensitive. I predict True.")
c = 'Subaru'
print(car == c.lower())

print("\nIs car == 'toyota'? I predict False.")
print(car == 'toyota')

number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)

print("\nIs number == 11? I predict False.")
print(number == 11)

print("\nIs number != 10? I predict True.")
print(number != 11)

print("\nIs number > 9 and <11? I predict True.")
print(number > 9 and number < 11)

print("\nIs number < 9 or >11? I predict False.")
print(number < 9 or number > 11)