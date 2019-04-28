# -*- encoding:utf-8 -*-

from flask import Flask

from junyi.model.factory import Factory

app = Flask(__name__)


@app.route("/factory/add")
def factory_add():
    return(Factory.add())

@app.route("/factory/search/")
def factory_search_all():
    return(Factory.search_all())

@app.route("/factory/search/<id>")
def factory_search_by_id(id):
    return(Factory.search_by_no())

@app.route("/factory/delete/<id>")
def factory_delete_by_id(id):
    return(Factory.delete_by_no())

@app.route("/factory/modify/<id>")
def factory_modify_by_id(id):
    return(Factory.modify())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9527", debug=True)