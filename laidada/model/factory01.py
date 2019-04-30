# -*- encoding:utf-8 -*-

from laidada.DB.db01 import factory_list
class Factory():

    @classmethod
    def add(cls, factory_info):
        factory_list.append(factory_info)
        factory_info['no'] = "00002"
        factory_info['status'] = "1"
        # ret = {"success": True, "info": factory_info}
        ret = {"success": False, "info": "Tel error"}
        return ret

    @classmethod
    def search_all(cls):
        return ("Factory-> search_all")

    @classmethod
    def search_by_no(cls, no):
        pass

    @classmethod
    def delete_by_no(cls, no):
        return ("Factory-> delete_by_no")

    @classmethod
    def modify(cls, no, name, city, address, contact, tel, worker):
        return ("Factory-> modify")