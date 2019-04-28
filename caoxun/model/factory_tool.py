# -*- encoding:utf-8 -*-
from caoxun.database.factory_db import factory_list

class Factory():

    @classmethod
    def add(cls,name,city,address,contact,tel,worker):
        #TODO 传入的数组按工厂数据格式进行整理
        pass
        #TODO 向现有工厂数据列表中插入新增的工厂数据
        pass
        #TODO 返回操作结果的状态：是否成功，返回新增工厂的编号
        # 成功：True, 1001
        # 失败：False，None
        factory = factory_list.append({"name": name, "city": "city", "address": address,\
                                        "contact": contact, "tel": tel,"worker": worker})

        return factory



    @classmethod
    def search_all(cls):
        #查询所有工厂列表
        # TODO 获取所有工厂的列表
        print(factory_list)
        # TODO 返回所有工厂的列表
        return factory_list



    @classmethod
    def search_by_no(cls,no):
        #根据工厂编号查询
        pass



    @classmethod
    def delete_by_no(cls,no):
        #根据工厂编号删除指定工厂信息
        return "Factory-> delete_by_no"



    @classmethod
    def modify(cls,name,city,address,contact,tel,works):
        # 根据工厂编号修改指定工厂的信息
        return "Factory-> modify"










