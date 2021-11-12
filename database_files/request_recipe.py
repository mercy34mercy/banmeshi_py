import requests
import time
from database_files.database import add_recipe, get_db

from database_files.request_rakuten import get_datas

def get_recipes():
  
  url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
  
  # カテゴリーAPIからjsonでデータを取得
  categorys  = get_db()
  
#   for category in categorys["data"]:
#     print(category["categoy"])

  jsonify = ({
          "data":[]
        })
  
  for category in categorys["data"]:
      params = {
      "format": "json",
      "applicationId": "1049614814076089333",
      "categoryId":category["categoy"],
      }
      
      
      responses = requests.get(url, params=params)
      jsondata = responses.json()  
  

  
  
      for data in jsondata["result"]:
            print("22")
            add_data = {
              "foodImageUrl":data["foodImageUrl"], 
              "mediumImageUrl":data["mediumImageUrl"],
              "recipeCost":data["recipeCost"],
              "recipeId":data["recipeId"],
              "recipeMaterial":data["recipeMaterial"],
              "recipeTitle":data["recipeTitle"],
              "recipeUrl":data["recipeUrl"],
              "smallImageUrl":data["smallImageUrl"]
            }
          
            jsonify["data"].append(add_data)
            time.sleep(5)
            #print(jsonify["data"])


    
  return jsonify


