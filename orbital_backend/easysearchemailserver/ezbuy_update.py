import requests
import pyrebase
from requests.exceptions import HTTPError
import update

def check(dict_item):
    if dict_item['item'] == "trending":
        keyword = dict_item['title']
    else:
        keyword = dict_item['item']
    price_initial = dict_item['price']
    title = dict_item["title"]
    ratings = dict_item["ratings"]
    img = dict_item["image"]
    ezbuy_url = dict_item["url"] 

    #Firebase configuration
    firebaseConfig = {"apiKey": "AIzaSyDuvbUVOCLozok7Fb4H7_e6xVtbXBFhBBw",
                      "authDomain": "team-cheapskate.firebaseapp.com",
                      "databaseURL": "https://team-cheapskate-default-rtdb.asia-southeast1.firebasedatabase.app",
                      "projectId": "team-cheapskate",
                      "storageBucket": "team-cheapskate.appspot.com",
                      "messagingSenderId": "823951002393",
                      "appId": "1:823951002393:web:1a7ff1774ac17316a55388",
                      "measurementId": "G-MPLZ3HJ3ZX"}

    #Initialising Firebase
    firebase = pyrebase.initialize_app(firebaseConfig)

    #Database
    db = firebase.database()

    try:
        url = 'https://sg-en-web-api.ezbuy.sg/api/EzCategory/ListProductsByCondition'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        data = {
            "searchCondition":
                {"categoryId": 0, "freeShippingType": 0,
                    "filter": [], "keyWords": keyword},
                "limit": 100,
                "offset": 0,
                "language": "en",
                "dataType": "new"
        }
        #access JSON content
        req = requests.post(url, headers=headers, json=data)
        jsonResponse = req.json()
        products = jsonResponse['products']

        #For non-trending products
        if dict_item['item'] != "trending":
            for product in products:
                url_updated =  f'www.ezbuy.sg/product/{product["url"]}'
                if url_updated == ezbuy_url:
                    try:
                        price = product['discountInfo']['price']
                    except:
                        price = "$" + str(round(product['price'], 2))
                    break
        else:
            for product in products:
                title_updated = product['name']
                if title == title_updated:
                    try:
                        price = product['discountInfo']['price']
                    except:
                        price = "$" + str(round(product['price'], 2))
                    break

        if float(price[1:]) >= float(price_initial[1:]):
            print("Higher/Same")
            update.realtime(
                [keyword, [title, price, ezbuy_url, img, ratings], "ezbuy"])
            dict_output = dict_item.copy()
            dict_output["price"] = price 
            return dict_item
        else:
            print("Lower")
            update.realtime(
                [keyword, [title, price, ezbuy_url, img, ratings], "ezbuy"])
            dict_output = dict_item.copy()
            dict_output["price"] = price
            return dict_output

    except Exception as err:
        print(f"Error/Not found, {err}")
        return dict_item

test_dict = {'image': 'https://i.ezbuy.sg/Fpi-JkR3dire2fqsF5lDQtFhqCBt',
             'item': 'airpods',
             'price': '$264.00',
             'ratings': '5 stars',
             'store': 'ezbuy',
             'url': 'www.ezbuy.sg/product/427301306',
             'title': '[On Sale] Apple AirPods Pro | 1 Year Local Singapore Warranty'}

#print(check(test_dict))
