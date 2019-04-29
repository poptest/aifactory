# -*- encoding=utf-8 -*-
# 创建工厂网页注册页面

from flask import Flask, request,render_template
from Kane.factory_model.factory_model import Factory

app = Flask(__name__)

@app.route("/factory")
def factory():
    return render_template("index.html")


# 添加工厂的网页
@app.route("/factory/add",methods=['POST','GET'])
def factory_add():
    if request.method=="GET":
        return render_template("factory.html")
    else:
        No = request.form.get('No')
        Facory_Name = request.form.get('Facory_Name')
        City = request.form.get('City')
        Address = request.form.get('Address')
        Contact = request.form.get('Contact')
        Tel = request.form.get('Tel')
        Worker = request.form.get('Worker')
        Status = request.form.get('Status')

        return render_template("factory_success.html",
                                No=No,
                                Facory_Name=Facory_Name,
                                City=City,
                                Address=Address,
                                Contact=Contact,
                                Tel=Tel,
                                Worker=Worker,
                                Status=Status)

# 查询所以工厂信息的网页
@app.route("/factory/search_all")
def factory_search_all():
    return (Factory.factory_search_all())


# 通过编号查询指定工厂的网页
@app.route("/factory/search_by_no/<no>")
def factory_search_by_id(no):
    return (Factory.factory_search_by_no())


# 通过编号删除指定的工厂的信息
@app.route("/factory/delect_by_no/<no>")
def factory_delect_by_no(no):
    return (Factory.factory_delect_by_no())


# 通过编号修改指定工厂的信息
@app.route("/factory/modif_by_no/<no>")
def factory_modif_by_no(no):
    return (Factory.factory_modif_by_no())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", debug=True)
