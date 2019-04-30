# -*- encoding:utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/factory/add/",methods=['GET','POST'])
def factory_add():
    req_method = request.method
    print ("User Reuqest method:%s"%req_method)
    if req_method == 'GET':
        return render_template("factory_add.html")
    else:
        no = 00001
        name = request.form.get("name")
        city = request.form.get("city")
        address = request.form.get("address")
        contact = request.form.get("contact")
        tel = request.form.get("tel")
        duijie = request.form.get("duijie")
        status = 1
        return render_template("factory_add_success.html",
                                no=no,
                                name = name,
                                city = city,
                                address = address,
                                contact = contact,
                                tel = tel,
                                duijie = duijie,
                                status = status
                               )


if __name__ == '__main__':
    app.run()