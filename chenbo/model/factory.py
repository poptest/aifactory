# -*- encoding:utf-8 -*-
from chenbo.db.factory_db import factory_list

class Factory():

    @classmethod
    def add(cls, name, city, address, contact, tel, worker):
        #新增一个工厂
        #TODO 传入的数组按工厂数据格式进行整理

        #TODO 向现有工厂数据列表中插入新增的工厂数据

        #TODO 返回操作结果的状态：是否成功，返回新增工厂的编号
        # 成功：True, 1001
        # 失败：False，None
        factory={"no":103,"name":name,"city":city,"address":address,"contanct":contact,"tel":tel,"worker":worker}
        factory_list.append(factory)
        return(str(factory["no"]))

    @classmethod
    def search_all(cls):
        #查询所有工厂列表
        #TODO 获取所有工厂的列表
        pass
        #TODO 返回所有工厂的列表


        return (str(factory_list))

    @classmethod
    def search_by_no(cls, no):
        #根据工厂编号，查询工厂信息
        sum=0
        for i in factory_list:
            if i["no"]==no:
                return (str(i))
            else:
                sum+=1



    @classmethod
    def delete_by_no(cls, no):
        #根据工厂编号删除指定工厂信息
        sum=0
        for i in factory_list:
            if i["no"]==no:
                factory_list.pop(sum)
                return (str(factory_list))
            else:
                sum+=1


    @classmethod
    def modify(cls, no, name, city, address, contact, tel, worker):
        #根据工厂编号修改指定工厂的信息
        sum = 0
        for i in factory_list:
            if i["no"] == no:
                i[sum]={"no":no,"name":name,"city":city,"address":address,"contact":contact,"tel":tel,"worker":worker}
                return (str(i[sum]))
            else:
                sum += 1

