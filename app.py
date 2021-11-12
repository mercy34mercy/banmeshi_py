# -*- coding: utf-8 -*-
from flask import Flask
from database_files.request_rakuten import get_datas
from database_files.database import initialize_db, add_db,get_db,get_db_recipe,initialize_recipe_db,add_recipe,get_db_recipe_one
from database_files.request_recipe import get_recipes
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, syunki'

@app.route('/hello')
def indexs():
    return 'hello'

@app.route('/init')
def init():
    try:
        initialize_db()
    except Exception as e:
        print('=== エラー内容 ===')
        print('type:' + str(type(e)))
        print('args:' + str(e.args))
        # print('message:' + e.message)
        
        
        print('error:' + str(e))
        return "error"
    return "success"

@app.route('/init_recipe')
def init_recipe():
    try:
        initialize_recipe_db()
    except Exception as e:
        print('=== エラー内容 ===')
        print('type:' + str(type(e)))
        print('args:' + str(e.args))
        # print('message:' + e.message)
        
        
        print('error:' + str(e))
        return "error"
    return "success"

#カテゴリにリクエストして、レシピをDBに保存
@app.route('/requestrakuten')
def requestrakuten():
    try:
        datas = get_datas()
        add_db(datas)
    except Exception as e:
        print('=== エラー内容 ===')
        print('type:' + str(type(e)))
        print('args:' + str(e.args))
        print('message:' + e.message)
        print('error:' + str(e))
        return e
    return "sucess"

@app.route('/requestrecipe')
def requestrecipe():
        try:
            datas = get_recipes()
            add_recipe(datas)
        except Exception as e:
            print('=== エラー内容 ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('error:' + str(e))
            return e
        return "sucess"

#DBから出力
@app.route('/getall')
def get_all():
    data = get_db()
    # datas = data.split("/")
    
    return data

@app.route('/getall_recipe')
def get_all_recipe():
    data = get_db_recipe()
    print(data)
    return "1"

@app.route('/get_db_recipe_one')
def get_recipe_one():
    data = get_db_recipe_one()
    print(data)
    return "2"


# helloooooooooo
if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port = 20)
    

