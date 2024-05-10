import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__,static_folder='static')


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
    return render_template('waterSystem.html')


@app.route('/dataCenter')
def dataCenter():
    return render_template('dataCenter.html')


@app.route('/smartCenter')
def smartCenter():
    return render_template('smartCenter.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)