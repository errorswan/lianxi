'''
8.1 定义函数练习
'''

'''
8-1 消息
'''

def display_message():
    """显示简单的描述"""
    print("我在本章学习的是定义函数")

display_message()


'''
8-2 喜欢的图书
'''
def favorite_book(title):
    """显示喜欢的书"""
    print("One of my favorite books is "+ title.title() + ".")

favorite_book('Alice in Wonderland')