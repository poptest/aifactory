# -*- encoding=utf-8 -*-
#创建工厂网页注册页面

from flask import Flask
from Kane.factory_model.factory_model import Factory

app=Flask(__name__)

#添加工厂的网页
@app.route("/factory/add")
def factory_add():
    return (Factory.factory_add())

#查询所以工厂信息的网页
@app.route("/factory/search_all")
def factory_search_all():
    return (Factory.factory_search_all())

#通过编号查询指定工厂的网页
@app.route("/factory/search_by_no/<no>")
def factory_search_by_id(no):
    return (Factory.factory_search_by_no())

#通过编号删除指定的工厂的信息
@app.route("/factory/delect_by_no/<no>")
def factory_delect_by_no(no):
    return (Factory.factory_delect_by_no())

#通过编号修改指定工厂的信息
@app.route("/factory/modif_by_no/<no>")
def factory_modif_by_no(no):
    return (Factory.factory_modif_by_no())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", debug=True)