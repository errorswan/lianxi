
"""8.3 返回值练习"""

'''
8-6 城市名
'''

def city_country(city, country):
    """整理城市格式"""
    full_city = city + ", " + country
    return full_city.title()

city_01 = city_country('santiago', 'chile')
print(city_01)

city_02 = city_country('beijing', 'china')
print(city_02)

city_03 = city_country('shanghai', 'china')
print(city_03)

'''
8-7 专辑
'''

def make_album(singer, album):
    """返回一个字典，接受歌手的名字和专辑名"""
    full_alum = {'singer': singer, 'album': album}
    return full_alum

a = make_album('jay', 'jay')
print(a)

b = make_album('jay', 'fantasy')
print(b)

c = make_album('jay', '八度空间')
print(c)

# 添加可选形参，存储专辑包含歌曲数
def make_album(singer, album, songs=''):
    """返回一个字典，接受歌手的名字和专辑名"""
    full_alum = {'singer': singer, 'album': album}
    if songs:
        full_alum['songs'] = songs
    return full_alum
a = make_album('jay', 'jay', 10)
print(a)

'''
8-8 用户的专辑数
'''

def make_album(singer, album):
    """返回一个字典，接受歌手的名字和专辑名"""
    full_alum = {'singer': singer, 'album': album}
    return full_alum

while True:
    print("\n请告诉我专辑信息：")
    print("\n输入'q'退出程序")

    si = input("歌手是： ")
    if si == 'q':
        break
    al = input("专辑名称是： ")
    if al == 'q':
        break

    ful_al = make_album(si, al)
    print(ful_al)