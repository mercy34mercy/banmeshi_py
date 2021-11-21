import sqlite3
import pandas as pd

def create():
    db = sqlite3.connect("recipe.db") #「hoge」を変更 
    df = pd.read_sql_query("SELECT*FROM RECIPE", db)#「table」を変更 
    db.close()
    df.to_csv("hoge.csv", index=None)
    
create()