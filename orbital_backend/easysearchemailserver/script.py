import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import amazon_update
import qoo10_update
import shopee_update
import ezbuy_update
import update
from time import sleep
from mailing_script import send_email

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#Get list of users in mailing list
def get_mailing_list_id():
    users_id = db.collection('users').get()
    return list(map(lambda x: x.id, users_id))

#Get wishlist
def get_wishlist(uid):
    wishlist = db.collection('users').document(
        uid).collection('wishlist').get()[0].to_dict()
    return wishlist["items"]

#Execute
def execute_send(mailing_list):
    try:
        counter = 0
        for user in get_mailing_list_id():
            try:
                print(user)
                user_email = get_email(user)
                wishlist = get_wishlist(user)
                collated_items = []
                for dict_item in wishlist:
                    if type(dict_item) == dict:
                        collated_items.append(website_checker(dict_item))
                        sleep(10)
            except:
                continue

            #Update firestore wishlist
            db.collection("users").document(user).collection('wishlist').document('arrayOfItems').update({'items' : collated_items})

            to_mail = mailed_items(wishlist, collated_items)
            if to_mail:
                send_email(user_email, to_mail)

            #Server sleep
            counter += 1
            if collated_items and counter < len(user) - 1:
                sleep(600)

    except Exception as err:
        raise(err)

    print("Task completed")

#Website checker to run API/crawl
def website_checker(dict_item):
    store = dict_item["store"]
    if store == "amazon":
        return amazon_update.check(dict_item)
    elif store == "qoo10":
        return qoo10_update.check(dict_item)
    elif store == "shopee":
        return shopee_update.check(dict_item)
    else:
        return ezbuy_update.check(dict_item) 

#Get email
def get_email(uid):
    return auth.get_user(uid).email

#Retrieving items to be mailed to user
def mailed_items(wishlist, collated_items):
    output = []
    for i in range(len(wishlist)):
        dict_item = wishlist[i]
        collated_item = collated_items[i]
        if collated_item['price'] < dict_item['price']:
            output.append(collated_item)
    return output


#Testing
execute_send(get_mailing_list_id())

