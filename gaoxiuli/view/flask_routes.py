# -*- encoding:utf-8 -*-

from flask import Flask, render_template, request
from gaoxiuli.model.factory import Factory


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/factory/add", methods=['GET', 'POST'])
def factory_add():
    req_method = request.method
    print("User Reuqest method: %s" % req_method)
    if req_method == 'GET':
        return render_template("factory_add.html")
    else:
        factory_data = {}
        factory_data["name"] = request.form.get("fac_name")
        factory_data["city"] = request.form.get("city")
        factory_data["address"] = request.form.get("address")
        factory_data["contact"] = request.form.get("contact")
        factory_data["tel"] = request.form.get("tel")
        factory_data["duijie"] = request.form.get("duijie")

        add_result = Factory.add(factory_data)
        add_result_if_success = add_result['success']
        add_result_info = add_result['info']
        if add_result_if_success == True:
            return render_template("factory_add_success.html", factory_info=add_result_info)
        else:
            return "Factory add error!, msg: %s" % add_result_info

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
