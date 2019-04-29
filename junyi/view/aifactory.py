# -*- encoding:utf-8 -*-

from flask import Flask, render_template, request

from junyi.model.factory import Factory

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
        no = "00001"
        name = request.form.get("fac_name")
        city = request.form.get("city")
        address = request.form.get("address")
        contact = request.form.get("contact")
        tel = request.form.get("tel")
        dj = request.form.get("dj")
        status="1"
        return render_template("factory_add_success.html",
                               no=no,
                               name=name,
                               city=city,
                               address=address,
                               contact=contact,
                               tel=tel,
                               dj=dj,
                               status=status)

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