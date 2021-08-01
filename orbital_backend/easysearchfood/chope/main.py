from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyrebase
import os
from time import sleep
import chromedriver_binary

scroll_pause_time = 1

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return "hello world!"

@app.route('/<keyword>/chope', methods=["GET", "POST"])
@cross_origin()
def chope_server(keyword):
    #Website URL
    chope_url = f"https://shop.chope.co/search?q={keyword}*&type=product"

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
        #Chrome Options
        options = webdriver.ChromeOptions()
        options.add_argument('headless') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("window-size=1024,768")

        #Initialising ChromeDriver
        browser = webdriver.Chrome(chrome_options = options)
        browser.get(chope_url)

        #Automate scrolling to work around lazy loading
        while True:
            last_height = browser.execute_script(
                'return document.body.scrollHeight')
            browser.execute_script('window.scrollTo(0, window.scrollY + 500);')
            sleep(scroll_pause_time)
            new_height = browser.execute_script(
                'return document.body.scrollHeight')

            if new_height == last_height:
                browser.execute_script(
                    'window.scrollTo(0, window.scrollY + 500);')
                sleep(scroll_pause_time)
                new_height = browser.execute_script(
                    'return document.body.scrollHeight')
                if new_height == last_height:
                    break
                else:
                    last_height = new_height
                    continue
       #Searching for relevant elements
        try:
            products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
                (By.XPATH, ".//div[contains(@class,'product-each-tile relative')]")))
        
        except:
            products = []

        #Data Wrangling
        collated = []
        for i in range(20):
            try:
                product = products[i]
                title = product.find_element_by_xpath(
                    ".//a[contains(@class,'color-blue app-link')]").text
                url = product.find_element_by_xpath(
                    ".//a[contains(@class,'color-blue app-link')]").get_attribute('href')
                img = product.find_element_by_xpath(
                    ".//img[contains(@class,'image lazy loaded')]").get_attribute('src')
                price = product.find_element_by_xpath(
                    ".//strong[contains(@class, 'price color-orange')]").text
                location = product.find_element_by_xpath(
                    ".//div[contains(@class, 'product-cuisine color-darkgrey mt-5')]").text
                discount = product.find_element_by_xpath(
                    ".//div[contains(@class, 'product-savings')]").text[1:] + " OFF" 
                collated.append([title, price, url, img, location, discount])
            except Exception as err:
                continue

        #Closing browser
        browser.quit()

        #Removing duplicate
        checker = []
        collated_updated = []
        for item in collated:
            if item[0] not in checker:
                collated_updated.append(item)
                checker.append(item[0])

        sorted_collated = collated[:10]

        #Handling for results with less than 10 products
        for i in range(10 - len(sorted_collated)):
            sorted_collated.append(['Nil', 'Nil', 'Nil', 'Nil', 'Nil', 'Nil'])
 
        #Adding data into firebase
        for i in range(len(sorted_collated)):
            recommended = sorted_collated[i]
            data = {"title": recommended[0],
                    "price": recommended[1],
                    "url": recommended[2],
                    "image": recommended[3],
                    "location": recommended[4],
                    "discount": recommended[5]
                    }
            db.child("easysearchfoodvoucher").child(keyword.lower()).child("chope").child(i+1).set(data)

        return "Task completed"

    except Exception as err:
        print(f'Unusual traffic network occured, {err}')
        browser.quit()
        return "Error"


def formatter(str_input):
    formatted = ""
    for char in str_input:
        if not char == ",":
            formatted += char
    return formatted

if __name__ == "__main__":
    app.run()

