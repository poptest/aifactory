# -*- encoding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/factory/add")
def factory_add():
    pass

@app.route("/factory/search/")
def factory_search_all():
    pass

@app.route("/factory/search/<id>")
def factory_search_by_id(id):
    pass

@app.route("/factory/delete/<id>")
def factory_delete_by_id(id):
    pass

@app.route("/factory/modify/<id>")
def factory_modify_by_id(id):
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9527", debug=True)