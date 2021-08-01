import requests
import pyrebase
from requests.exceptions import HTTPError


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
        for product in products:
            name = product['name']
            try:
                price = product['discountInfo']['price']
            except:
                price = "$" + str(round(product['price'], 2))
            url = f'www.ezbuy.sg/product/{product["url"]}'
            img = product['picture']
            ratings = f'{product["leftView"]["rateScore"]} stars'

            try:
                num_sold = int(product['rightView']['text'].split(" ")[0])
            except:
                num_sold = 0
            collated.append([name, price, url, num_sold, img, ratings])

        #Sorting data
        sorted_collated = sorted(
            collated, key=lambda x: float(x[1][1:]), reverse=True)[:10]
        sorted_collated = sorted(
            sorted_collated, key=lambda x: x[3], reverse=True)[:3]

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
            db.child(keyword.lower()).child("ezbuy").child(i+1).set(data)

        print("Task completed")

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        raise(err)
        print(f'Other error occurred: {err}')
