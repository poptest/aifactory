#encoding: utf-8

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html" )

@app.route("/factory/add",methods=['GET','POST'])
def factory_add():
    req_method = request.method
    print("User Request method:%s" % req_method)
    if req_method=="GET":
        return render_template("factory_add.html")
    else:
        return render_template("factory_add.success.html")

if __name__=='__main__':
    app.run()