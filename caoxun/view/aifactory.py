# -*- encoding:utf-8 -*-

from flask import Flask
from caoxun.model.factory_tool import Factory
from caoxun.database.factory_db import factory_list

app = Flask(__name__)


@app.route('/factory/add/')
def factory_add():
    name = "demo5"
    city = "daye"
    address = "option valley"
    contact = "Hua Hua"
    tel = "1555555555"
    worker = "Xiao Lai"
    return str(Factory.add(name,city,address,contact,tel,worker))



@app.route('/factory/search/')
def factory_search_all():
    all = Factory.search_all()
    return str(all)


@app.route('/factory/search/<id>')
def factory_search_by_id():
    return(Factory.search_by_no())


@app.route("/factory/delete/<id>")
def factory_delete_by_id(id):
    return(Factory.delete_by_no())


@app.route("/factory/modify/<id>")
def factory_modify_by_id(id):
    return(Factory.modify())




if __name__ == '__main__':
  app.run()







