"""9.5 Python 标准库练习"""

'''9-13 使用OrderedDict'''

from collections import OrderedDict

vocabulary = OrderedDict()

vocabulary['列表'] = '由一系列按特定顺序排列的元素组成。'
vocabulary['for循环'] = '对列表中的每个元素都执行相同的操作。'
vocabulary['if语句'] = '条件测试语句。'
vocabulary['字典'] = '一系列键-值对。'
vocabulary['切片'] = '处理列表的部分元素。'
vocabulary['变量'] = '储存一个与变量相关信息的值'
vocabulary['字符串'] = '就是一系列字符,用引号括起的都是字符串'
vocabulary['元组'] = '不能修改的值称为不可变的，而不可变的列表 称为元组'
vocabulary['条件测试'] = '一个值为True或False的表达式称为条件测试'
vocabulary['浮点数'] = '将带小数点的数字都称为浮点数'

for key,value in vocabulary.items():
    print(key + ":" + value)

'''9-14 骰子'''

from random import randint

class Die():

    def __init__(self, sides=6):
        """n面的骰子"""
        self.sides = sides

    def roll_die(self):
        """掷10次"""
        t = 0
        while t < 10:
            x = randint(1, self.sides + 1)
            print(str(x))
            t += 1

# 6面骰子掷10次
my_d6 = Die()
my_d6.roll_die()
# 10面骰子掷10次
my_d6 = Die(10)
my_d6.roll_die()
# 20面骰子掷10次
my_d6 = Die(20)
my_d6.roll_die()