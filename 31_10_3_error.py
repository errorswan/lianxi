"""10.3 异常练习"""

'''10-6 加法运算'''

print("输入两个数字，求和")
print("输入 q 退出")

while True:
    try:
        first_number = input("请输入第一个数字：")
        if first_number == 'q':
            break

        first_number = int(first_number)

        second_number = input("请输入第二个数字：")
        if second_number == 'q':
            break

        second_number = int(second_number)

    except ValueError:
        print("请输入数字而不是文本。")

    else:
        answer = first_number + second_number
        print("两个数字的和为" + str(answer))

'''10-7 加法计算器'''
# 如上

'''10-8 猫和狗'''

def read_name(filename):

    try:
        with open(filename) as f_obj:
            content = f_obj.read()

    except FileNotFoundError:
        print("对不起 " + filename + " 文件不存在。")

    else:
        print(content)

filenames = ['cats.txt', 'dogs.txt', 'pig.txt']
for filename in filenames:
    read_name(filename)

'''10-9 沉默的猫和狗'''

def read_name(filename):

    try:
        with open(filename) as f_obj:
            content = f_obj.read()

    except FileNotFoundError:
        pass

    else:
        print(content)

filenames = ['cats.txt', 'dogs.txt', 'pig.txt']
for filename in filenames:
    read_name(filename)

'''10-10 常见单词'''

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    words = contents.lower().count('row')
    print(words)
