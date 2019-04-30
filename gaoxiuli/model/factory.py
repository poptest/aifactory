# -*- encoding:utf-8 -*-
from gaoxiuli.db.factory_db import factory_list

class Factory():

    @classmethod
    def add(cls, factory_info):
        # 新增一个工厂
        # {"success":True, info:{工厂的信息字典，包括no，status}}
        # {"success":False, info:"失败的原因"}
        # TODO 向现有工厂数据列表中插入新增的工厂数据
        factory_list.append(factory_info)

        factory_info['no'] = "00002"
        factory_info['status'] = "1"
        # ret = {"success": True, "info": factory_info}
        ret = {"success": False, "info": "Tel error"}
        return ret

    @classmethod
    def search_all(cls):
        #查询所有工厂列表
        #TODO 获取所有工厂的列表
        pass
        #TODO 返回所有工厂的列表

        return ("Factory-> search_all")

    @classmethod
    def search_by_no(cls, no):
        #根据工厂编号，查询工厂信息
        pass

    @classmethod
    def delete_by_no(cls, no):
        #根据工厂编号删除指定工厂信息
        return ("Factory-> delete_by_no")

    @classmethod
    def modify(cls, no, name, city, address, contact, tel, worker):
        #根据工厂编号修改指定工厂的信息
        return ("Factory-> modify")