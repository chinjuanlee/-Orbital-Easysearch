from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyrebase
import os
from time import sleep

amazon_urls = {"Technology": "https://www.amazon.sg/gp/bestsellers/electronics/ref=zg_bs_nav_0",
               "Health, Household & Personal Care": "https://www.amazon.sg/gp/bestsellers/hpc/ref=zg_bs_nav_0",
               "Beauty": "https://www.amazon.sg/gp/bestsellers/beauty/ref=zg_bs_nav_0",
               "Fashion": "https://www.amazon.sg/gp/bestsellers/fashion/ref=zg_bs_nav_0",
               "Food": "https://www.amazon.sg/gp/bestsellers/grocery/ref=zg_bs_nav_0"
               }


def trending_call(category, amazon_url):

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
        browser.get(amazon_url)

        #Searching for relevant elements
        products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, ".//span[contains(@class,'aok-inline-block zg-item')]")))

        #Data Wrangling
        collated = []
        for i in range(10):
            try:
                product = products[i]
                title = product.find_element_by_xpath(
                    ".//div[contains(@class,'p13n-sc-truncated')]").text
                price_variable = product.find_elements_by_xpath(
                    ".//span[contains(@class,'p13n-sc-price')]")
                if len(price_variable) > 1:
                    price_lower = price_variable[0].text[1:]
                    price_higher = price_variable[1].text[1:]
                    price = price_lower + " - " + price_higher
                else:
                    price = price_variable[0].text[1:]
                url = product.find_element_by_xpath(
                    ".//a[contains(@class,'a-link-normal')]").get_attribute('href')
                img = product.find_element_by_xpath(
                    ".//div[contains(@class,'a-section a-spacing-small')]//img").get_attribute("src")
                try:
                    ratings = product.find_element_by_xpath(
                        ".//div[contains(@class,'a-icon-row a-spacing-none')]//a").get_attribute("title")[:3] + " stars"
                except:
                    ratings = "No stars given"
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
                "amazon").child(i+1).set(data)

        browser.quit()

    except Exception as err:
        print(f'Unusual traffic network occured, {err}')
        browser.quit()


for key, value in amazon_urls.items():
    try:
        trending_call(key, value)
    except:
        continue
