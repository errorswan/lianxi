'''
6.4 嵌套练习
'''

'''
6-7 人
'''

people_01 = {'first_name': 'Don', 'last_name': 'Hu', 'age': 28, 'city': 'Yongkang'}
people_02 = {'first_name': 'Xiaoxiao', 'last_name': 'Su', 'age': 25, 'city': 'Yongkang'}
people_03 = {'first_name': 'Yifu', 'last_name': 'Yao', 'age': 28, 'city': 'Yongkang'}

people = [people_01, people_02, people_03]
for p in people:
    print(p)

'''
6-8 宠物
'''

dog = {'type': 'dog', 'master': 'don'}
cat = {'type': 'cat', 'master': 'xiaoxiao'}
rat = {'type': 'rat', 'master': 'Fu'}

pets = [dog, cat, rat]
for pet in pets:
    print(pet)

'''
6-9 喜欢的地方
'''

favorite_places = {'don': ['japan', 'england', 'france'],
                   'xiaoxiao': ['usa', 'germany', 'france'],
                   'fu': ['japan', 'korea', 'usa'],
                    }
for name,places in favorite_places.items():
    print("\n" + name.title() + "'s favorite place are:")
    for place in places:
        print("\t" + place.title())

'''
6-10 喜欢的数字
'''

favorite_number = {'Don': [7, 8, 9],
                   'Xiaoxiao': [8, 9, 0],
                   'Li': [5, 6, 7],
                   'Fu': [3, 4, 5],
                   'Yao': [6, 7,8]
                   }
for name,numbers in favorite_number.items():
    print("\n" + name.title() + "'s favorite number is:")
    for number in numbers:
        print("\t" + str(number))


'''
6-11 城市
'''

cities = {'beijing': {'country': 'china',
                      'population': '21 million',
                      'fact': 'The capital of China.'
                      },
            'shanghai': {'country': 'china',
                         'population': '24 million',
                         'fact': 'The most developed city in China'
                        },
            'tokyo': {'country': 'japan',
                      'population': '13 million',
                      'fact': 'The largest city in the world.'
                      }

            }
for cityname,city_info in cities.items():
    print("\nCity:" + cityname)
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("\tCountry: " + country.title())
    print("\tPopulation: " + population)
    print("\tFact: " + fact)

'''
6-12 扩展
'''

# 通过查看len（language）的值来确定当前被调查者喜欢的语言是否有多种
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite languages is:")  # 如果只有一种，修改输出措辞
        print("\t" + languages[0].title())
    elif len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
