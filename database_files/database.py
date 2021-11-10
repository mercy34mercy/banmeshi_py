import csv
import sqlite3
import json

db_path = "banmeshi.db"			# データベースファイル名を指定
db_path_recipe = "recipe.db"


def initialize_db():
    con = sqlite3.connect(db_path)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    # small {"categoryName":"しめさば","parentCategoryId":"72","categoryId":2026,"categoryUrl":"https://recipe.rakuten.co.jp/category/11-72-2026/"}
    # medium {"categoryName":"牛肉","parentCategoryId":"10","categoryId":275,"categoryUrl":"https://recipe.rakuten.co.jp/category/10-275/"}
    # large {"categoryName":"西洋料理","categoryId":"25","categoryUrl":"https://recipe.rakuten.co.jp/category/25/"}
    cur.execute('''CREATE TABLE BANMESHI
		(categoryName text primary key,
		parentCategoryId text,
		categoryId text,
		categoryUrl text,
        category text)''')
    # cur.execute('''CREATE TABLE BANMESHI
  #              (categoryName text, parentCategoryId text, categoryId text, categoryUrl real)''')

    con.commit()					# データベース更新の確定
    con.close()						# データベースを閉じる
    
    
# foodImageUrl
# mediumImageUrl
# nickname
# pickup
# rank
# recipeCost
# recipeDescription
# recipeId
# recipeIndication
# recipeMaterial
# recipePublishday
# recipeTitle
# recipeUrl
# shop
# smallImageUrl

def initialize_recipe_db():
    con = sqlite3.connect(db_path_recipe)
    cur = con.cursor()
    cur.execute('''CREATE TABLE RECIPE
                (foodImageUrl text,
                mediumImageUrl text,
                recipeCost text,
                recipeId text,
                recipeMaterial text,
                recipeTitle text,
                recipeUrl text,
                smallImageUrl text)''')
    
    con.commit()					# データベース更新の確定
    con.close()						# データベースを閉じる
    
    
def add_recipe(jsondata):
    con = sqlite3.connect(db_path_recipe)
    cur = con.cursor()
    print(jsondata)
    
    
    jsondata = "{'result': [{'foodImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg', 'mediumImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg?thum=54', 'nickname': 'はぁぽじ', 'pickup': 0, 'rank': '1', 'recipeCost': '300円前後', 'recipeDescription': 'そのままでも、ご飯にのせて丼にしても♪', 'recipeId': 1760028309, 'recipeIndication': '約10分', 'recipeMaterial': ['鶏むね肉', '塩', '酒', '片栗粉', '○水', '○塩', '○鶏がらスープの素', '○黒胡椒', '長ネギ', 'いりごま', 'ごま油'], 'recipePublishday': '2017/10/10 22:37:34', 'recipeTitle': 'ご飯がすすむ！鶏むね肉のねぎ塩焼き', 'recipeUrl': 'https://recipe.rakuten.co.jp/recipe/1760028309/', 'shop': 0, 'smallImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/fbd7dd260d736654532e6c0b1ec185a0cede8675.49.2.3.2.jpg?thum=55'}, {'foodImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/3e5906a3607b2f1321cda1158b251c4223204420.40.2.3.2.jpg', 'mediumImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/3e5906a3607b2f1321cda1158b251c4223204420.40.2.3.2.jpg?thum=54', 'nickname': '*ももら*', 'pickup': 1, 'rank': '2', 'recipeCost': '300円前後', 'recipeDescription': '鶏胸肉なのにウイング風♬骨が無いので食べ易くお弁当にもピッタリ♡油で揚げないのでヘルシーです♪', 'recipeId': 1400014946, 'recipeIndication': '約10分', 'recipeMaterial': ['鶏むね肉', '片栗粉', '塩コショウ', '炒め用サラダ油', 'A醤油', 'Aみりん', 'Aお酒', 'A砂糖'], 'recipePublishday': '2015/09/30 14:28:09', 'recipeTitle': '鶏胸肉で簡単♪手羽風揚げない甘辛照焼チキンお弁当に', 'recipeUrl': 'https://recipe.rakuten.co.jp/recipe/1400014946/', 'shop': 0, 'smallImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/3e5906a3607b2f1321cda1158b251c4223204420.40.2.3.2.jpg?thum=55'}, {'foodImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/aedd5fa798b463b0371dceb8e3d0f529e4dc1b48.79.2.3.2.jpg', 'mediumImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/aedd5fa798b463b0371dceb8e3d0f529e4dc1b48.79.2.3.2.jpg?thum=54', 'nickname': 'く〜-Qoo-', 'pickup': 0, 'rank': '3', 'recipeCost': '500円前後', 'recipeDescription': '好評の為レシピを分かりやすくしました。\n分量を多少変更しました。（２０１３年３月）\n以前載せていたポテサラパケットは\nレシピID: 1590004701です。', 'recipeId': 1590002716, 'recipeIndication': '約1時間', 'recipeMaterial': ['【ハンバーグ材料】', '牛豚合びき肉', '豚ひき肉', '玉ねぎ', 'パン粉', '卵', '塩', '胡椒', 'マヨネーズ', '合わせ味噌', 'ナツメグ', 'コーヒーフレッシュ', '【ハンバーグソース材料】', '玉ねぎ', 'みかんやオレンジの果汁', '水', '醤油', '料理酒', 'みりん', '【サラダ】', '大根', '人参', 'レタスか白菜', 'サウザンドレッシング（ダイムドレ代用）', '醤油マヨ', '炒りごま', 'ミニトマト'], 'recipePublishday': '2012/01/27 21:13:53', 'recipeTitle': '元店長がこっそり教えるびっくり◯ンキーのハンバーグ', 'recipeUrl': 'https://recipe.rakuten.co.jp/recipe/1590002716/', 'shop': 0, 'smallImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/aedd5fa798b463b0371dceb8e3d0f529e4dc1b48.79.2.3.2.jpg?thum=55'}, {'foodImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/2fd4ee7c388118c811c7c340377961862fee4a72.20.2.3.2.jpg', 'mediumImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/2fd4ee7c388118c811c7c340377961862fee4a72.20.2.3.2.jpg?thum=54', 'nickname': 'グルヤマ', 'pickup': 1, 'rank': '4', 'recipeCost': '指定なし', 'recipeDescription': 'お酢を使って手羽元を炒め煮にしました。\nにんにくとしょうががうまさのポイントです。', 'recipeId': 1570002039, 'recipeIndication': '指定なし', 'recipeMaterial': ['鶏手羽元', '卵（ゆでたまご）', 'にんにく', 'しょうが', '酒', '酢', 'しょうゆ', '砂糖', 'みりん'], 'recipePublishday': '2011/03/26 08:45:33', 'recipeTitle': 'お酢で疲労回復☆手羽元のさっぱり煮', 'recipeUrl': 'https://recipe.rakuten.co.jp/recipe/1570002039/', 'shop': 0, 'smallImageUrl': 'https://image.space.rakuten.co.jp/d/strg/ctrl/3/2fd4ee7c388118c811c7c340377961862fee4a72.20.2.3.2.jpg?thum=55'}]}"
    jsondata = jsondata.json()

    for size in range(len( jsondata["result"])):
        data = jsondata["result"][size]
        if(data == "recipeMaterial"):
            for l in  range(len(data)):
                text += data[recipeMaterial][l].text + ','
                
        print(text)
    
    
            
       
            
            
    try:
        cur.execute('insert into RECIPE(foodImageUrl,mediumImageUrl,recipeCost,recipeId,recipeMaterial,recipeTitle,recipeUrl,smallImageUrl) values (?,?,?,?,?,?,?,?);', (data["foodImageUrl"],data["mediumImageUrl"],data["recipeCost"],data["recipeId"],text,data["recipeTitle"],data["recipeUrl"],data["smallImageUrl"]))
    except:
        try:
            cur.execute('update RECIPE set foodImageUrl=? ,mediumImageUrl=? ,recipeCost=? ,recipeMaterial=? ,recipeTitle=? ,recipeUrl=? ,smallImageUrl=?  where recipeId = ?',(data["foodImageUrl"],data["mediumImageUrl"],data["recipeCost"],text,data["recipeTitle"],data["recipeUrl"],data["smallImageUrl"],data["recipeId"]))
        except Exception as e:
            print('=== エラー内容 ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('message:' + e.message)
            print('error:' + str(e))
            return e
          
                        
    con.commit()					# データベース更新の確定
    con.close()						# データベースを閉じる
    


def add_db(responses):
    con = sqlite3.connect(db_path)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    # SQL文の実行
    # try:
    for response in responses:
        for category in responses[response]:
            for data in responses[response][category]:
                if(category!='large'):
                    try:
                        cur.execute('insert into BANMESHI(categoryName,parentCategoryId,categoryId,categoryUrl,category) values (?,?,?,?,?);', (data["categoryName"],data["parentCategoryId"],data["categoryId"],data["categoryUrl"],category))
                    except:
                        try:
                            cur.execute('update BANMESHI set parentCategoryId=? ,categoryId=?, categoryUrl=?, category=? where categoryName=?',(data["parentCategoryId"],data["categoryUrl"],data["categoryId"],category,data["categoryName"]))
                        except Exception as e:
                            print('=== エラー内容 ===')
                            print('type:' + str(type(e)))
                            print('args:' + str(e.args))
                            print('message:' + e.message)
                            print('error:' + str(e))
                            return e       
                elif(category=='large'):
                    try:
                        cur.execute('insert into BANMESHI(categoryName,parentCategoryId,categoryId,categoryUrl,category) values (?,0,?,?,?);', (data["categoryName"],data["categoryId"],data["categoryUrl"],category))
                    except:
                        try:
                            cur.execute('update BANMESHI set parentCategoryId=0 ,categoryId=?, categoryUrl=?, category=? where categoryName=?',(data["categoryUrl"],data["categoryId"],category,data["categoryName"]))
                        except Exception as e:
                            print('=== エラー内容 ===')
                            print('type:' + str(type(e)))
                            print('args:' + str(e.args))
                            print('message:' + e.message)
                            print('error:' + str(e))
                            return e       
    # except sqlite3.Error as e:		# エラー処理
    #     print("Error occurred:", e.args[0])

    con.commit()					# データベース更新の確定
    con.close()						# データベースを閉じる


def get_db():
    data = []
    con = sqlite3.connect(db_path)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    cur.execute('SELECT categoryName FROM BANMESHI')
    datas=cur.fetchall()
    for data in datas:
        print(data)
    # try:
    #      for row in cur.execute('SELECT * FROM BANMESHI'):
    #         print(row)
    #         data.append(row)
    # except sqlite3.Error as e:		# エラー処理
    #     print("Error occurred:", e.args[0])
    #     return e
    return data


def get_db_recipe():
    data  = []
    con = sqlite3.connect(db_path_recipe)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    cur.execute('SELECT * FROM RECIPE')
    datas=cur.fetchall()
    for data in datas:
        print(data)
    return data

def get_db_one(category):
    con = sqlite3.connect(db_path)  # データベースに接続
    cur = con.cursor()				# カーソルを取得
    # cur.execute('SELECT * FROM BANMESHI where "%{}%"'.format(category))
    result=cur.execute('SELECT * FROM BANMESHI where categoryName = "クリスマスケーキ"')
    for row in cur:
        print(row)
# get_db()
# get_db_one("ケーキ")



add_recipe("jsondata")