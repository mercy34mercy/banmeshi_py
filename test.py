

from database_files.request_recipe import get_recipes
from database_files.database import initialize_db, add_db,get_db,get_db_recipe,initialize_recipe_db,add_recipe

def test():
    datas = get_recipes()
    add_recipe(datas)
    
    return datas


test()