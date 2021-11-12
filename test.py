import requests
import time
from database_files.database import add_recipe, get_db

from database_files.request_rakuten import get_datas
from database_files.request_recipe import get_recipes


  
a = get_recipes()
add_recipe(a)
