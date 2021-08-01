import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore

def realtime(item_updated):

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

    #Retrieving existing data
    keyword = item_updated[0]
    website = item_updated[2]

    doc = db.child("airpods").child(website).get()
    num_checker = 0
    for i in range(1, 4):
        item_updated_name = item_updated[1][0]
        db_item_name = doc.each()[i].val()["title"]
        if item_updated_name == db_item_name:
            num_checker = i

    data = {"title": item_updated[1][0],
            "price": item_updated[1][1],
            "url": item_updated[1][2],
            "image": item_updated[1][3],
            "ratings": item_updated[1][4]
            }

    if num_checker != 0:
        db.child(keyword).child(website).child(num_checker).set(data)

    print("Task complete")

