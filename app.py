import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__,static_folder='static')


@app.route('/')
def index():
    return render_template('layout.html')

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