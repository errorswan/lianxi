'''
7.3 while 循环处理列表和字典练习
'''

'''
7-8 熟食店
'''
sandwich_orders = ['Manwich', 'Maxwell Street Polish', 'Melt sandwich']
finished_sandwiches = []

while sandwich_orders:
    curren_sandwishes = sandwich_orders.pop()
    print("I made your " + curren_sandwishes + ".")
    finished_sandwiches.append(curren_sandwishes)

print("\nThe following sandwiches have been made :")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

'''
7-9 五香烟熏牛肉（pastrami）卖完了
'''
sandwich_orders = ['Pastrami', 'Manwich', 'Pastrami', 'Maxwell Street Polish', 'Melt sandwich', 'Pastrami']
print("\nPastrami have been sold out!")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

finished_sandwiches = sandwich_orders[:]
print(finished_sandwiches)

'''
7-10 梦想的度假胜地
'''

holiday = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, where would you go?")
    holiday[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")

    if repeat == 'no':
        active = False

print("\n--- Poll Results ---")
for name,response in holiday.items():
    print(name + " would like to go for holiday" + response + ".")