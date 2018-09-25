'''
4-1 披萨
'''
pizzas = ['new york', 'chicago', 'california', 'pan', 'thick']
for pizza in pizzas:
    print(pizza.title() + " pizza")

# 打印包含披萨的句子
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.")

# 总结性句子
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.")
print("\nI really love pizza!")

'''
4-2 动物
'''
animal = ['dog', 'cat', 'rabbit']
for pet in animal:
    print(pet)

# 针对每种动物打印一个句子
for pet in animal:
    print("A "+ pet + " would make a great pet.")

# 总结性句子
for pet in animal:
    print("A "+ pet + " would make a great pet.")
print("\nAny of these animals would make a great pet!")