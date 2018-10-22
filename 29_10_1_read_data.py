"""10.1从文件中读取数据"""

'''10-1 Python 学习笔记'''

filename = 'learning_python.txt'

with open(filename) as file_object:
    content = file_object.read()
    print(content)

''''''
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

''''''
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line)

'''10-2 C语言学习笔记'''
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        line = line.rstrip()
        print(line.replace('Python', 'C'))
