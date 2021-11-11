import requests

from request_rakuten import get_datas

def get_recipes():
  
  url = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
  
  # カテゴリーAPIからjsonでデータを取得
  categorys  = get_datas()
  
  for category in categorys:
      params = {
      "format": "json",
      "applicationId": "1049614814076089333",
      "categoryId":category,
  }
    
  responses = requests.get(url, params=params)
  jsondata = responses.json()  
  
  jsonify = ({
        "data":[]
        })
  try:
    for data in jsondata["result"]:
      jsonify["data"].append(data)
  except:
    print("エラー")


    
    
      

  
  return jsondata
 


# a = get_recipes()
# print(a)
