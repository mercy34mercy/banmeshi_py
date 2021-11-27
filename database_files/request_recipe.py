import requests
import time
from database_files.database import add_recipe, get_db


def get_recipes():
  a = 0  
  url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
  
  # カテゴリーAPIからjsonでデータを取得
  categorys  = get_db()
  
# for category in categorys["data"]:
#   print(category["categoy"])


  
  for category in categorys["data"]:
      params = {
      "format": "json",
      "applicationId": "1049614814076089333",
      "categoryId":category["categoy"],
      }
      time.sleep(15)
      
      responses = requests.get(url, params=params)
      jsondata = responses.json()  
  

  
      
      for data in jsondata["result"]:
              jsonify = ({
                "data":[]
            })
              a += 1
              print(a)
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
              try:
                add_recipe(jsonify)
              except:
                i = 0
    
              


    
  return jsonify


