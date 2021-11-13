import requests
import time
from database_files.database import add_recipe, get_db

from database_files.request_rakuten import get_datas
from database_files.request_recipe import get_recipes
import sqlite3
import json
from typing import Text

db_path = "banmeshi.db"			# データベースファイル名を指定


  
def get():
    data = []
    con = sqlite3.connect(db_path)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    cur.execute('SELECT COUNT(*) FROM BANMESHI')
    datas=cur.fetchall()
    print(datas)



get()
