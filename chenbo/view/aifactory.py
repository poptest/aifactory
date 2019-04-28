# -*- encoding:utf-8 -*-

from flask import Flask

from chenbo.model.factory import Factory

app = Flask(__name__)
@app.route("/")
def stu():
    return "hello."

@app.route("/factory/add")
def factory_add():
    name="demo1"
    city="黄冈"
    address="qichun"
    contact="老王"
    tel="15917171717"
    worker="小张"

    return(Factory.add(name,city,address,contact,tel,worker))

@app.route("/factory/search/")
def factory_search_all():
    return(Factory.search_all())

@app.route("/factory/search/<id>")
def factory_search_by_id(id):
    return(Factory.search_by_no(102))

@app.route("/factory/delete/<id>")
def factory_delete_by_id(id):

    return(Factory.delete_by_no(100))

@app.route("/factory/modify/<id>")
def factory_modify_by_id(id):
    no=100
    name = "demo1"
    city = "黄冈"
    address = "qichun"
    contact = "老王"
    tel = "15917171717"
    worker = "小张"
    return(Factory.modify(no,name,city,address,contact,tel,worker))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="555", debug=True)