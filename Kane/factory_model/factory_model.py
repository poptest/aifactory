# -*- encoding=utf-8 -*-
from Kane.factory_db.factory_db import factory_list


# 新建一个工厂类，里面包含增，删，改，查操作
class Factory():

    # 添加工厂信息的方法
    @classmethod
    def factory_add(name, city, address, contact, tel, worer):
        # TODO 传入的数据根据工厂表的格式进行调整
        pass

        # TODO 向现有工厂数据库插入数据
        pass

        # TODO 返回操作结果，是否成功，返回新增的工厂编号
        pass

    # 查询所有工厂的方法
    @classmethod
    def factory_search_all(self):
        # TODO  获取所有的列表信息
        for factory in factory_list:
            # TODO 显示所有列表的信息
            no = str(factory["No"])
            name = factory["工厂名称"]
            city = factory["城市"]
            address = factory["地址"]
            contact = factory["联系人"]
            tel = factory["联系人电话"]
            worker = factory["对接人"]
            status = factory["账号状态"]
            return "编号:%s---工厂名字:%s---城市:%s---地址：%s---联系人：%s---联系人电话：%s---对接人：%s---账号状态：%s" % (
            no, name, city, address, contact, tel, worker, status)

    # 通过编号查询指定工厂信息
    @classmethod
    def factory_search_by_no(no):
        # TODO 根据编号查询指定工厂的信息

        for factory in factory_list:
            No = ""
            name = ""
            city = ""
            address = ""
            contact = ""
            tel = ""
            worker = ""
            status = ""
            if str(factory["No"]) == no:
                break
            No = str(factory["No"])
            name = factory["工厂名称"]
            city = factory["城市"]
            address = factory["地址"]
            contact = factory["联系人"]
            tel = factory["联系人电话"]
            worker = factory["对接人"]
            status = factory["账号状态"]

            return "编号:%s---工厂名字:%s---城市:%s---地址：%s---联系人：%s---联系人电话：%s---对接人：%s---账号状态：%s" % (
    No, name, city, address, contact, tel, worker, status)


    # 通过编号删除指定工厂信息
    @classmethod
    def factory_delect_by_no(no):
        # TODO 通过编号删除指定工厂的信息
        index = 0
        for factory in factory_list:
            if str(factory['No']) == no:
                factory_list.pop(index)
            else:
                index += 1


    # 通过编号修改指定的工厂信息
    @classmethod
    def factory_modif_by_no(no, name, city, address, contact, tel, worer):
        # TODO 通过指定的编号修改指定的工厂的信息
        pass
