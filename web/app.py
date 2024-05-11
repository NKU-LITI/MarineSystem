import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from flask import Flask, render_template, request, url_for, redirect
from data import SourceData

app = Flask(__name__,static_folder='static')
source = SourceData()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # 在这里处理登录逻辑
    print('email:',email,' password:',password)

    return redirect(url_for('mainInfo'))


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    # 在这里处理注册逻辑
    print('name:',name,' email:',email,' password:',password)

    return redirect(url_for('index'))


@app.route('/reset-password')
def reset_password():
    return '<h1>Coming Soon!<h1>'


@app.route('/mainInfo')
def mainInfo():
    return render_template('mainInfo.html')


@app.route('/waterSystem')
def waterSystem():
    data = source.pie
    data2= source.line
    xAxis = data2.pop('legend')
    data3=source.line2
    return render_template('waterSystem.html', title='水下系统', data=data, legend=[i.get('name') for i in data], data2=data2, legend2=list(data2.keys()),xAxis=xAxis, data3=data3,)


@app.route('/dataCenter')
def dataCenter():
    return render_template('dataCenter.html')


@app.route('/smartCenter')
def smartCenter():
    return render_template('smartCenter.html')


@app.route('/admain')
def admain():
    return render_template('admain/login.html')




@app.route('/do_admain_login', methods=['POST'])
def do_admain_login():
    # 这里可以添加验证逻辑，验证管理员身份（用户名和密码）
    # 如果验证成功，重定向到新页面
    return redirect(url_for('admain_main'))


@app.route('/admain_main')
def admain_main():
    return render_template('admain/main.html')


@app.route('/admain_left')
def admain_left():
    return render_template('admain/left.html')

@app.route('/admain_top')
def admain_top():
    return render_template('admain/top.html')

@app.route('/admain_index')
def admain_right():
    return render_template('admain/index.html')

@app.route('/admain_default')
def admain_default():
    return render_template('admain/default.html')

@app.route('/admain_operateList')
def admain_operateList():
    return render_template('admain/operateList.html')
    
@app.route('/admain_searchList')
def admain_searchList():
    return render_template('admain/searchList.html')

@app.route('/admain_form')
def admain_form():
    return render_template('admain/form.html')

@app.route('/admain_tab')
def admain_tab():
    return render_template('admain/tab.html')

@app.route('/admain_imgtable')
def admain_imgtable():
    return render_template('admain/imgtable.html')

@app.route('/admain_imglist')
def admain_imglist():
    return render_template('admain/imglist.html')

@app.route('/admain_imglist1')
def admain_imglist1():
    return render_template('admain/imglist1.html')

@app.route('/admain_tools')
def admain_tools():
    return render_template('admain/tools.html')

@app.route('/admain_filelist')
def admain_filelist():
    return render_template('admain/filelist.html')

@app.route('/admain_computer')
def admain_computer():
    return render_template('admain/computer.html')

@app.route('/admain_error')
def admain_error():
    return render_template('admain/error.html')



@app.route('/logout_success')
def logout_success():
    return render_template('mainInfo.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

