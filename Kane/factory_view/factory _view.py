# -*- encoding=utf-8 -*-
# 创建工厂网页注册页面

from flask import Flask, request
from Kane.factory_model.factory_model import Factory

app = Flask(__name__)


# 添加工厂的网页
@app.route("/factory/add",methods=['POST','GET'])
def factory_add():
    if request.method=="GET":

        html_page = '''
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title></title>
                </head>
                <body>
                    <form action="" method="post" >
                        <h1 align="center">工厂注册系统</h1>
                        <table align="center" border="1px" cellspacing="0px" width="50%" height="500px">
                            <tr>
                                <td><font color="red">编号</font></td>
                                <td>
                                    <input type="number" placeholder ="请输入编号" name="No"/>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">工厂名称</font></td>
                                <td>
                                    <input type="text" placeholder ="请输入工厂名称" name="Facory_Name"/>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">城市</font></td>
                                <td>
                                    <select name="City">
                                        <option value="武汉">武汉</option>
                                        <option value="广东">广东</option>
                                        <option value="北京">北京</option>
                                        <option value="上海">上海</option>
                                        <option value="南京">南京</option>
                                        <option value="福建">福建</option>
                                        <option value="长沙">长沙</option>
                                        <option value="深圳">深圳</option>
                                        <option value="郑州">郑州</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">地址</font></td>
                                <td>
                                    <textarea cols="50" rows="3" maxlength="50" placeholder ="请输入地址" name="Address"></textarea>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">联系人</font></td>
                                <td>
                                    <input type="text" placeholder ="请输入联系人"  name="Contact"/>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">联系人电话</font></td>
                                <td>
                                    <input type="number" maxlength="11" placeholder ="请输入联系电话" name="Tel"/>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">对接人</font></td>
                                <td>
                                    <input type="text" placeholder ="请输入对接人" name="Worker"/>
                                </td>
                            </tr>
                            <tr>
                                <td><font color="red">账号状态</font></td>
                                <td>
                                    <input type="radio" name="Status"  value="启用"/>启用
                                    <input type="radio" name="Status"  value="停用" checked/>停用
                                    <input type="radio" name="Status"  value="注销"/>注销
                                </td>
                            </tr>
                            <tr>
                                <td colspan="2" align="center">
                                    <input type="submit" value="注册"/>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                                    <input type="reset" value="重置" />&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                                    <button>登录</button>
                                </td>
                            </tr>
                        </table>
                    </form>
                     
                </body>
            </html>
        '''
        return (html_page)
    else:
        No=request.form.get('No')
        Facory_Name=request.form.get('Facory_Name')
        City=request.form.get('City')
        Address=request.form.get('Address')
        Contact=request.form.get('Contact')
        Tel=request.form.get('Tel')
        Worker=request.form.get('Worker')
        Status=request.form.get('Status')
        msg="NO->%s  Facory_Name->%s  City->%s  Address->%s  Contact->%s  Tel->%s  Worker->%s  Status->%s"%(No, Facory_Name, City, Address, Contact, Tel, Worker, Status)
        return msg
    # return (Factory.factory_add())


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
