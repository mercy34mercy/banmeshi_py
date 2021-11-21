# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from database_files.database import get_db_recipe_one


app = Flask(__name__)


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

#カテゴリにリクエストして、レシピをDBに保存
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



@app.route('/get_db_recipe_one',methods=['POST','GET'])
def get_recipe_one():
    if request.method == 'POST':
        print(request.json)
        data = get_db_recipe_one(request.json["data"])
        print(data)
    else:
        return "method POST ONLY"


    return data






