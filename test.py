import requests
import time
import psycopg2
import json
from typing import Text
		

DATABASE_URL = 'postgres://aiddbjmxylnjxm:d0d3756986638bd8f399a370d3aace891221c4bffb21c4543c3e65f2d25e7cd0@ec2-54-225-187-177.compute-1.amazonaws.com:5432/der1lubvsuh4mb'# データベースファイル名を指定
  
def get():
    data = []
    con = psycopg2.connect(DATABASE_URL, sslmode='require')# データベースに接続
    cur = con.cursor()				# カーソルを取得
    cur.execute('SELECT * FROM BANMESHI')
    datas=cur.fetchall()
    print(datas)



get()
