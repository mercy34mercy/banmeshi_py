
import json
from database_files.request_recipe import get_recipes
from database_files.database import initialize_db, add_db,get_db,get_db_recipe,initialize_recipe_db,add_recipe

def test():
    #datas = get_recipes()
    datas = open("data.json","r")
    print(datas)
    
    

    data = json.load(datas)
    add_recipe(data)
    
    return data


test()