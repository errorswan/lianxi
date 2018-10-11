"""8.5 传递任意数量的实参"""

'''8-12 三明治'''

def make_sandwich(*toppings):
    """打印顾客点的三明治"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('bread','salad','vegetables' )

'''8-13 用户简介'''

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('don', 'hu',
                            location='shanxi',
                            field='biology',
                             job='home')
print(user_profile)

'''8-14 汽车'''

def make_car(manufacturer, type, **car_info):
    """创建一个字典，包含一辆汽车的所有信息"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['type'] = type
    for key,value in car_info.items():
        profile[key] = value
    return profile

car = make_car('ford', 'kuga',
                color='black',
                tow_package='sunroof')
print(car)