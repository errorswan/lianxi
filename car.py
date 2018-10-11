def make_car(manufacturer, type, **car_info):
    """创建一个字典，包含一辆汽车的所有信息"""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['type'] = type
    for key,value in car_info.items():
        profile[key] = value
    return profile