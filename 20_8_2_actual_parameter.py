'''
8.2 传递实参练习
'''

'''
8-3 T恤
'''

def make_shirt(size,word):
   """显示T恤尺码和字样"""
   print("The T-shirt is size " + size + " and the words " + word + ".")

make_shirt("L","SB")
make_shirt(size='L', word='SB')

'''
8-4 大号T恤
'''

def make_shirt(size='L',word='I love Python'):
   """显示T恤尺码和字样"""
   print("The T-shirt is size " + size + " and the words " + word + ".")

make_shirt()
make_shirt(size='M',)
make_shirt(size="XL", word="I love PC")

'''
8-5 城市
'''
def describe_city(name,country='China'):
    """显示城市和所属国家"""
    print(name.title() + " belongs to " + country.title())

describe_city('beijing')
describe_city('shanghai')
describe_city('totyo', 'japan')