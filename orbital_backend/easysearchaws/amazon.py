import requests
from bs4 import BeautifulSoup, SoupStrainer
import pyrebase
import random

def crawl(keyword):

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

    url = f"https://www.amazon.sg/s?k={keyword}&ref=nb_sb_noss"
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    int_random = random.randint(0,4)
    headers = {'User-Agent': user_agent_list[int_random]}
 
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")
    items = soup.find_all("div", {"class": "a-section a-spacing-medium"})
    collated = []
    best_sellers = []
    for item in items:
        try:
            title = item.find(
                "span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
            try:
                badge = item.find("span", {"class": "a-badge-text"}).text
                print(badge)
                if badge =="Amazon's " or badge == "Best Seller":
                    pass
                else:
                    badge = "Not included"
            except:
                badge = "Not included"
            url = 'https://amazon.sg' + \
                item.find(
                    "a", {"class": "a-link-normal a-text-normal"})['href']
            img = item.find("img", {"class": "s-image"})['src']
            price_whole = item.find("span", {"class": "a-price-whole"}).text
            price_fraction = item.find(
                "span", {"class": "a-price-fraction"}).text
            price = formatter(f"${price_whole}{price_fraction}")
            review_bar = item.find(
                "div", {"class": "a-section a-spacing-none a-spacing-top-micro"})
            review = formatter(review_bar.find(
                "span", {"class": "a-size-base"}).text)
            ratings = item.find(
                "div", {"class": "a-row a-size-small"}).find('span')['aria-label']
            ratings = f'{float(ratings[:3])} stars'
            collated.append([title, price, url, review, img, ratings])
            if badge != "Not included":
                best_sellers.append([title, price, url, review, img, ratings])
            continue
        except Exception as err:
            continue
        
    sorted_collated = best_sellers.copy()

    #Removing duplicate
    checker = []
    collated_updated = []
    for item in collated:
        if item[0] not in checker:
            collated_updated.append(item)
            checker.append(item[0])

    temporary = sorted(
        collated_updated, key=lambda x: float(x[1][1:]), reverse=True)
    temporary = sorted(
        temporary, key=lambda x: int(x[3]), reverse=True)

    counter = 0
    while len(sorted_collated) < 5:
        try:
            item_temp = temporary[counter]
            if item_temp not in sorted_collated:
                sorted_collated.append(item_temp)
        except:
            break
        counter += 1

    #Handling for results with less than 5 products
    for i in range(5 - len(sorted_collated)):
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
        db.child(keyword.lower()).child("amazon").child(i+1).set(data)

    print(sorted_collated)
    return "Task completed"


def formatter(str_input):
    formatted = ""
    for char in str_input:
        if not char == ",":
            formatted += char
    return formatted
