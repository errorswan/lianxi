'''
7.1 input()原理练习
'''

'''
7-1 汽车租赁
'''

car = input("What kind of car do you want to rent： " )
print("Let me see if I can find you a " + car)


'''
7-2 餐馆订位
'''
people = input("How many people do you have for dinner: ")
people = int(people)

if people >8 :
    print("Sorry, we don't have enough tables.")
else:
    print("We have enough empty tables for dinner.")

'''
7-3 10的整数倍
'''

number = input("Enter a number, and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of 10.")
else:
    print("\nThe number " + str(number) + " is not a multiple of 10.")