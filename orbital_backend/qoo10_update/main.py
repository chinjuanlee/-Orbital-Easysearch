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

scroll_pause_time = 0.5

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return "hello world!"

@app.route('/<keyword>/qoo10', methods=["GET", "POST"])
@cross_origin()
def crawl(keyword):
    #Website URL
    fave_url = f"https://www.qoo10.sg/s/{keyword}?keyword={keyword}&keyword_auto_change="

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

    #Formatter
    def formatter(str_input):
        formatted = ""
        for char in str_input:
            if not char == ",":
                formatted += char
        return formatted


    try:
        #Chrome Options
        options = webdriver.ChromeOptions()
        options.add_argument('headless') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument('user-agent={0}'.format(user_agent))

        #Initialising ChromeDriver
        browser = webdriver.Chrome(chrome_options = options)
        browser.get(fave_url)

        #Automate scrolling to work around lazy loading
        for i in range(10):
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
 
        #Locating products
        try:
            products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
                (By.XPATH, ".//*[contains(@list_type,'search_new_list_type')]")))
        
        except:
            products = []
        
        collated = []
        
        for i in range(len(products)):
            try:
                product = products[i]
                title = product.find_element_by_xpath(
                    ".//div[@class='sbj']/a").get_attribute('title')
                if title[:6] == "Brand:":
                    continue
                url = product.find_element_by_xpath(
                    ".//div[@class='sbj']/a").get_attribute('href')
                img = product.find_element_by_xpath(
                    ".//div[@class='inner']/a/img").get_attribute('src')
                price = product.find_element_by_xpath(
                    ".//div[@class='prc']/strong").text[1:]
                price = formatter(price)
                try:
                    review = (product.find_element_by_xpath(
                        ".//a[@class='lnk_rv']").text[7:-1])
                except:
                    review = "0"
                try:
                    ratings = str((product.find_element_by_xpath(
                        ".//span[@class='rate_v']").get_attribute('title')[8])) + " stars"
                except:
                    ratings = "No ratings given"

                if review == '999+':
                    review = '999'

                collated.append([title, price, url, review, img, ratings])

            except Exception as err:
                continue
        
        browser.quit()
        #Removing duplicate
        checker = []
        collated_updated = []
        for item in collated:
            if item[0] not in checker:
                collated_updated.append(item)
                checker.append(item[0])

        sorted_collated = sorted(
            collated_updated, key=lambda x: float(x[1][2:]), reverse=True)[:20]
        sorted_collated = sorted(
            sorted_collated, key=lambda x: int(x[3]), reverse=True)[:5]

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

            db.child(keyword.lower()).child("qoo10").child(i+1).set(data)

        return "Task completed"

    except Exception as err:
        browser.quit()
        return f"Error occurred, {err}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

