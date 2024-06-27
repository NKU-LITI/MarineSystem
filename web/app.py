import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from flask import Flask, render_template, request, url_for, redirect, jsonify


# 数据库相关
#from data import SourceData
from data_db import SourceData, ENGINE_CONFIG   # 主要用于前端界面的查询
#from data_db import db,Fish  # 主要用于admin的CRUD
from sqlalchemy import text

# openai相关
from openai import OpenAI
import requests

# 初始化数据库
app = Flask(__name__,static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE_CONFIG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
source = SourceData()
#db.init_app(app)


# bool变量控制查询操作
#Fish_Find = False
#Fish_Find_Data = []


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

    data_bream = source.line_bream
    data_roach = source.line_roach
    data_whitefish = source.line_whitefish
    data_parkki = source.line_Parkki
    data_perch = source.line_Perch
    data_pike = source.line_Pike
    data_smelt = source.line_Smelt
    data_height = source.line_height
    xAxis = data_height.pop('height')


    total_count = source.TotalCount
    growth_count = source.GrowthCount
    no_growth_count = source.NoGrowthCount
    fish_species = source.FishSpecies


    #return render_template('waterSystem.html', title='水下系统', data=data, legend=[i.get('name') for i in data], data2=data2, legend2=list(data2.keys()),xAxis=xAxis, data3=data3,)
    return render_template('waterSystem.html', title='水下系统', data=data, legend=[i.get('name') for i in data], 
                           data_bream=data_bream, data_roach=data_roach, data_whitefish=data_whitefish, data_parkki=data_parkki, 
                           data_perch=data_perch, data_pike=data_pike, data_smelt=data_smelt, data_height=data_height, legend2=list(data_height.keys()), xAxis = xAxis, 
                           total_count=total_count, growth_count= growth_count, no_growth_count = no_growth_count, fish_species = fish_species)

@app.route('/dataCenter')
def dataCenter():
    data = source.pie
    supply = source.water_supply #补充数据2021.4
    chinaDatas = [[{'name': item['省份'], 'value': item['水质类别']}] for item in supply]
    print(chinaDatas)

    yield_data = source.yield_data
    basin_data = [{'省份': item['省份'], '流域': item['流域'], 
                  '温度': item['温度'], 'PH': item['PH'], '站点情况': item['站点情况']} for item in supply]
    all_yield = source.all_yield
    return render_template('dataCenter.html', title='数据中心', data=data, legend=[i.get('name') for i in data],
                           supply=supply, chinaDatas=chinaDatas, yield_data=yield_data, basin_data=basin_data, all_yield=all_yield)


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


# admin: 鱼类表的展示及操作
# -------------------------------begin-------------------------------
@app.route('/admain_fish')
def admain_fish():
    fish = source.all_fish
    return render_template('admain/fish.html', all_fish=fish)

@app.route('/edit_fish', methods=['POST'])
def edit_fish():
    print("\n1\n")
    fish_id = request.form['id']
    species = request.form['species']
    weight = request.form['weight']
    length = request.form['length']
    height = request.form['height']
    width = request.form['width']
    status = request.form['status']
    print("\n2\n")
    source.update_fish(fish_id, species, weight, length, height, width, status)
    print("\n3\n")
    return redirect(url_for('admain_fish'))

@app.route('/delete_fish/<int:id>', methods=['POST'])
def delete_fish(id):
    print("\n1  {id}\n")
    source.delete_fish(fish_id=id)
    return redirect(url_for('admain_fish'))


@app.route('/insert_fish', methods=['POST'])
def insert_fish():
    species = request.form.get('species')
    weight = request.form.get('weight')
    length = request.form.get('length')
    height = request.form.get('height')
    width = request.form.get('width')
    status = request.form.get('status')

    source.insert_fish(species, weight, length, height, width, status)
    print("\n3\n")
    return redirect(url_for('admain_fish'))


@app.route('/search_fish', methods=['GET', 'POST'])
def search_fish():
    if request.method == 'POST':
        search_id = request.form.get('searchId')
        search_species = request.form.get('searchSpecies')
        search_weight = request.form.get('searchWeight')
        search_length = request.form.get('searchLength')
        search_height = request.form.get('searchHeight')
        search_width = request.form.get('searchWidth')
        search_status = request.form.get('searchStatus')
    elif request.method == 'GET':
        search_id = request.args.get('searchId')
        search_species = request.args.get('searchSpecies')
        search_weight = request.args.get('searchWeight')
        search_length = request.args.get('searchLength')
        search_height = request.args.get('searchHeight')
        search_width = request.args.get('searchWidth')
        search_status = request.args.get('searchStatus')

    # 构建 SQL 查询语句
    sql_query = "SELECT * FROM fish WHERE 1=1"

    # 添加条件：如果 search_species 不为空，则添加物种条件
    if search_id:
        sql_query += f" AND id = {search_id}"

    if search_species:
        sql_query += f" AND Species = '{search_species}'"

    # 添加条件：如果 search_status 不为空，则添加状态条件
    if search_status:
        sql_query += f" AND Status = '{search_status}'"

    # 添加条件：如果不为 0，则添加
    if search_weight and float(search_weight) != 0:
        sql_query += f" AND Weight = {float(search_weight)}"

    if search_length and float(search_length) != 0:
        sql_query += f" AND Length = {float(search_length)}"

    # 添加条件：如果 search_height 不为 0，则添加高度条件
    if search_height and float(search_height) != 0:
        sql_query += f" AND Height = {float(search_height)}"

    # 添加条件：如果 search_width 不为 0，则添加宽度条件
    if search_width and float(search_width) != 0:
        sql_query += f" AND Width = {float(search_width)}"

    print(sql_query)
    with source.ENGINE.connect() as conn:
        result = conn.execute(text(sql_query)).fetchall()
    fish_list = [dict(row._mapping) for row in result]
    print(fish_list)

    return render_template('admain/fish.html', all_fish=fish_list)


# -------------------------------begin-------------------------------


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

# 大模型API（用于回答）
api_key = "sk-Z6ttNnGzWksu7LYIOVVNuvXi3GqD5g6rykmK7NAn7ZcqTP7Q"
MessageModel = OpenAI(api_key=api_key, base_url="https://api.moonshot.cn/v1")


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    print("question:",user_message)

    # 构建消息列表
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    # 调用OpenAI API
    completion = MessageModel.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )


    # 直接访问ChatCompletionMessage对象的content属性
    model_reply = completion.choices[0].message.content
    # model_reply = get_reply(user_message)
    print("answer:",model_reply)
    return jsonify({'reply': model_reply})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

