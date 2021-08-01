import requests
import pyrebase
from requests.exceptions import HTTPError
from time import sleep

def api_call(keyword):
    collated = []

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
        url = "https://shopee.sg/api/v4/search/search_items?by=relevancy&keyword=" + keyword + "&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
        response = requests.get(url)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()

        for item in jsonResponse['items']:
            name = item['item_basic']['name']
            price_min = "$" + str(round(item['item_basic']['price_min'] / 100000, 2))
            url = f"https://shopee.sg/product/{item['shopid']}/{item['itemid']}"
            num_sold = item['item_basic']['historical_sold']
            img_id = item['item_basic']['image']
            img = f'https://cf.shopee.sg/file/{img_id}'
            ratings = f'{round(item["item_basic"]["item_rating"]["rating_star"], 2)} stars'
            collated.append([name, price_min,url, num_sold, img, ratings])

        #Sorting data
        sorted_collated = sorted(collated, key = lambda x : float(x[1][1:]), reverse = True)[:10]
        sorted_collated = sorted(sorted_collated, key = lambda x : x[3], reverse = True)[:3]

        #Handling for results with less than 3 products
        for i in range(3 - len(sorted_collated)):
            sorted_collated.append(['Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil'])
       
        #Adding data into firebase
        for i in range(len(sorted_collated)):
            recommended = sorted_collated[i]
            data = {"title": recommended[0],
                    "price": recommended[1],
                    "url": recommended[2],
                    "image": recommended[4],
                    "ratings": recommended[5]
                    }
            db.child(keyword.lower()).child("shopee").child(i+1).set(data)

        print("Task completed")
                

        
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}') 

api_call("airpods")
