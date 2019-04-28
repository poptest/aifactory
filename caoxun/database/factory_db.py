# -*- encoding:utf-8 -*-
'''
no: 工厂编号
name：工厂名称
city：城市
address：地址
contact：联系人
tel：联系人电话
worker：对接人
status: 1:启用，0，停用，-1，注销
'''

factory_list = [
    {"no": 1, "name": "demo1", "city": "wuhan", "address": "option valley", "contact": "ZHANG San", "tel": "1999999999",
        "worker": "Li Si", "status": "1"},
    {"no": 2, "name": "demo2", "city": "huangshi", "address": "option valley", "contact": "Xiao Ming", "tel": "1888888888",
        "worker": "Xiao Hong", "status": "1"},
    {"no": 3, "name": "demo3", "city": "hefei", "address": "option valley", "contact": "Wang Wu", "tel": "1777777777",
        "worker": "Xiao Hua", "status": "1"},
    {"no": 4, "name": "demo4", "city": "changsha", "address": "option valley", "contact": "Xiao Zi", "tel": "1666666666",
        "worker": "Xiao Lai", "status": "1"}
]

print(factory_list)