import requests
import json

# 郵便番号APIのURL
# https://zipcloud.ibsnet.co.jp/doc/api/search?zipcode=7830060

url = "https://zipcloud.ibsnet.co.jp/api/search"

# ユーザーから郵便番号の入力を受け取る
zip = input("郵便番号を入力=>")


param = {"zipcode": zip}

res = requests.get(url, params=param)


data = json.loads(res.text)

print(data)


if data["results"] is not None:
    address_info = data['results'][0]
    
    zipcode = address_info['zipcode']
    
    address = f"{address_info['address1']}{address_info['address2']}{address_info['address3']}"
    
    print(f"郵便番号:{zipcode}")
else:
    print("住所が見つかりませんでした")


