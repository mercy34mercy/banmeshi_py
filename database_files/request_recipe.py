import requests
import json
def get_recipes():
  
  url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
   

  params = {
      "format": "json",
      "applicationId": "1093061721945645180",
      "categoryId":"10",
  }
  

  responses = requests.get(url, params=params)
  jsondata = responses.json()
  

  
  
  
  #[0]が商品画像
  for size in range(len( jsondata["result"])):
    for l in jsondata["result"][size]:
      if l == "foodImageUrl" or l == "recipeCost"  or l == "recipeTitle" or l == "recipeUrl":
        print(l,jsondata["result"][size][l])
      elif l == "recipeMaterial":
        for k in range(len(jsondata["result"][size][l])):
          print(jsondata["result"][size][l][k])
  
  return responses
 

get_datas()