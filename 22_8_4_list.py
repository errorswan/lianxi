"""8.4 传递列表"""

'''
8-9 魔术师
'''

unprinted_magicians = ['liuqian', 'dawei', 'don']
show_magicians = []

while unprinted_magicians:
    magicians = unprinted_magicians.pop()
    print("\n魔术师名字： " + magicians)
    show_magicians.append(magicians)

print("\n以下的魔术师名字已经打印：")
for magician in show_magicians:
    print(magician)

'''
8-10 了不起的魔术师
'''
def make_great(unprinted_magicians, show_magicians):
    """
    模拟打印每个魔术师名字，直到没有未打印的魔术师为止
    打印每个魔术师后，都将其移到列表show_magicians中
    """
    while unprinted_magicians:
        magicians = unprinted_magicians.pop()
        print("\n魔术师名字： " + magicians.title())
        show_magicians.append("the Great " + magicians.title())

def pm(show_magicians):
    print("\n以下的魔术师名字已经打印：")
    for magician in show_magicians:
        print(magician)

unprinted_magicians = ['liuqian', 'dawei', 'don']
show_magicians = []

make_great(unprinted_magicians, show_magicians)
pm(show_magicians)

print(show_magicians)

'''
8-11 不变的魔术师
'''

def make_great(unprinted_magicians, show_magicians):
    """
    模拟打印每个魔术师名字，直到没有未打印的魔术师为止
    打印每个魔术师后，都将其移到列表show_magicians中
    """
    while unprinted_magicians:
        magicians = unprinted_magicians.pop()
        print("\n魔术师名字： " + magicians.title())
        show_magicians.append("the Great " + magicians.title())

def pm(show_magicians):
    print("\n以下的魔术师名字已经打印：")
    for magician in show_magicians:
        print(magician)

unprinted_magicians = ['liuqian', 'dawei', 'don']
show_magicians = []

make_great(unprinted_magicians[:], show_magicians)
pm(show_magicians)

print(unprinted_magicians)
print(show_magicians)