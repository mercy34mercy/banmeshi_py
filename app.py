# -*- coding: utf-8 -*-
from flask import Flask
from database_files.request_rakuten import get_datas
from database_files.database import initialize_db, add_db,get_db
from database_files.make_HTML import make_html
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello, world'

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

#DBから出力
@app.route('/getall')
def get_all():
    data = get_db()
    return make_html(data)


# helloooooooooo
if __name__ == '__main__':
    
    app.run()
