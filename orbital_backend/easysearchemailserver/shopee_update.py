import requests
import pyrebase
from requests.exceptions import HTTPError
from time import sleep
import update

def check(dict_item):
    keyword = dict_item['item']
    price_initial = dict_item['price']
    title = dict_item["title"]
    ratings = dict_item["ratings"]
    img = dict_item["image"]
    shopee_url = dict_item["url"] 

    try:
        url = "https://shopee.sg/api/v4/search/search_items?by=relevancy&keyword=" + keyword + "&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
        response = requests.get(url)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()

        for item in jsonResponse['items']:
            url_updated = f"https://shopee.sg/product/{item['shopid']}/{item['itemid']}"
            if url_updated == shopee_url:
                price =  "$" + str(round(item['item_basic']['price_min'] / 100000, 2))
                break

        if float(price[1:]) >= float(price_initial[1:]):
            print("Higher/Same")
            update.realtime(
                [keyword, [title, price, shopee_url, img, ratings], "shopee"])
            dict_output = dict_item.copy()
            dict_output["price"] = price 
            return dict_item
        else:
            print("Lower")
            update.realtime(
                [keyword, [title, price, shopee_url, img, ratings], "shopee"])
            dict_output = dict_item.copy()
            dict_output["price"] = price
            return dict_output
                        
    except Exception as err:
        print(f'Error/Not Found, {err}')
        return dict_item

test_dict = {'image': 'https://cf.shopee.sg/file/3578ce5ac446faaac78db04463052298',
             'item': 'airpods',
             'price': '$259.0',
             'ratings': '4.94 stars',
             'store': 'shopee',
             'url': 'https://shopee.sg/product/52377417/4308391777',
             'title': 'Apple Airpods Pro (Local Set)'}

#print(check(test_dict))
