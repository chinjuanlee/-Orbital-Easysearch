from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyrebase
import os
from time import sleep

ezbuy_urls = {"Technology": "https://ezbuy.sg/active/5ebb6919222e9b644e23af00/bestseller-ezbuy.html?NavBar=BS&ezspm=1.10000000.4.0.Best%20Seller&tag=floor_pos_1592968650242_%5BDigital%5D",
              "Health, Household & Personal Care": "http://ezbuy.sg/active/5ebb6919222e9b644e23af00/bestseller-ezbuy.html?NavBar=BS&ezspm=1.10000000.4.0.Best%20Seller&tag=floor_pos_1592968650242_%5BHome%5D",
              "Beauty": "http://ezbuy.sg/active/5ebb6919222e9b644e23af00/bestseller-ezbuy.html?NavBar=BS&ezspm=1.10000000.4.0.Best%20Seller&tag=floor_pos_1592968650242_%5BBeauty%5D",
              "Fashion": "http://ezbuy.sg/active/5ebb6919222e9b644e23af00/bestseller-ezbuy.html?NavBar=BS&ezspm=1.10000000.4.0.Best%20Seller&tag=floor_pos_1592968650242_%5BFashion%5D",
              "Food": "http://ezbuy.sg/active/5ebb6919222e9b644e23af00/bestseller-ezbuy.html?NavBar=BS&ezspm=1.10000000.4.0.Best%20Seller&tag=floor_pos_1592968650242_%5BGroceries%5D"
              }


def trending_call(category, ezbuy_url):

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
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")

        #Initialising ChromeDriver
        browser = webdriver.Chrome(
            options=options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        browser.get(ezbuy_url)
        sleep(5)

        #Searching for relevant elements
        products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//*[@id='floor_pos_1592968650242']/div/div[3]")))[0]
        products = products.find_elements_by_xpath(
            ".//a[contains(@target, '_blank')]")

        #Data Wrangling
        collated = []
        for i in range(10):
            try:
                product = products[i]
                title = product.find_element_by_xpath(
                    ".//p[contains(@class,'index_nameViews_4_1AJac')]").text
                price = product.find_element_by_xpath(
                    ".//span[contains(@class, 'index_currentPrice_3YCr3')]").text
                url = product.get_attribute('href')
                img = product.find_element_by_xpath(
                    ".//img[contains(@class, 'index_productImage_B5jxk')]").get_attribute('src')
                ratings = "5 stars"
                collated.append([title, price, url, img, ratings])
            except Exception as err:
                continue

        #Adding data into firebase
        for i in range(5):
            recommended = collated[i]
            data = {"title": recommended[0],
                    "price": recommended[1],
                    "url": recommended[2],
                    "image": recommended[3],
                    "ratings": recommended[4]
                    }
            db.child("trending").child(category).child(
                "ezbuy").child(i+1).set(data)

        browser.quit()

    except Exception as err:
        raise(err)
        print(f'Unusual traffic network occured, {err}')
        browser.quit()


for key, value in ezbuy_urls.items():
    try:
        trending_call(key, value)
    except:
        continue

