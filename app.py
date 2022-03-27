# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask_cors import CORS
from database_files.database import  get_db_recipe_one, random_one, random_one_by_mate, rollback
from database_files.request_recipe import get_recipes


app = Flask(__name__)
CORS(app)

@app.route('/',methods=['POST','GET'])
def index():
    print("リクエスト:" , request.json)
    if request.method == 'POST':
        top_key = request.json['query'] 
        num = request.json["num"]
    elif request.method == 'GET':
        top_key = "GETです"
        num = 0
    
    print(top_key)
    print(num)
    return 'hello, world'


@app.route('/recipeintodb',methods=['POST','GET'])
def intodb():
    get_recipes()
    return "sucess"

@app.route('/rollback',methods=['POST','GET'])
def roll():
    rollback()
    return "sucess"




# @app.route('/init')
# def init():
#     try:
#         initialize_db()
#     except Exception as e:
#         print('=== エラー内容 ===')
#         print('type:' + str(type(e)))
#         print('args:' + str(e.args))
#         # print('message:' + e.message)
        
        
#         print('error:' + str(e))
#         return "error"
#     return "success"

# @app.route('/init_recipe')
# def init_recipe():
#     try:
#         initialize_recipe_db()
#     except Exception as e:
#         print('=== エラー内容 ===')
#         print('type:' + str(type(e)))
#         print('args:' + str(e.args))
#         # print('message:' + e.message)
        
        
#         print('error:' + str(e))
#         return "error"
#     return "success"

# カテゴリにリクエストして、レシピをDBに保存
# @app.route('/requestrakuten')
# def requestrakuten():
#     try:
#         datas = get_datas()
#         add_db(datas)
#     except Exception as e:
#         print('=== エラー内容 ===')
#         print('type:' + str(type(e)))
#         print('args:' + str(e.args))
#         print('message:' + e.message)
#         print('error:' + str(e))
#         return e
#     return "sucess"

# @app.route('/requestrecipe')
# def requestrecipe():
#         try:
#             datas = get_recipes()
#         except Exception as e:
#             print('=== エラー内容 ===')
#             print('type:' + str(type(e)))
#             print('args:' + str(e.args))
#             print('message:' + e.message)
#             print('error:' + str(e))
#         return "sucess"


#DBから出力
# @app.route('/getall')
# def get_all():
#     data = get_db()
#     # datas = data.split("/")
    
#     return data

# @app.route('/getall_recipe')
# def get_all_recipe():
#     data = get_db_recipe()
#     print(data)
#     return "1"



@app.route('/get_recipe',methods=['POST'])
def get_recipe_one():
    if request.method == 'POST':
        print(request.json)
        data = get_db_recipe_one(request.json["data"])

    return data

@app.route('/random_one',methods=['GET'])
def random():
    data = random_one()
    return data
    
@app.route('/random_one_by_mate',methods=['POST'])
def random_by_recipe():
    data = random_one_by_mate(request.json)
    return data








