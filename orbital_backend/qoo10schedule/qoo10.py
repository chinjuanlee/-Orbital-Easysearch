from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyrebase
import os
from time import sleep

qoo10_urls = {"Technology": "//*[@id='ul_bestseller_group_category']/li[5]/a",
              "Health, Household & Personal Care": "//*[@id='ul_bestseller_group_category']/li[6]/a",
              "Beauty": "//*[@id='ul_bestseller_group_category']/li[3]/a",
              "Fashion": "//*[@id='ul_bestseller_group_category']/li[2]/a",
              "Food": "//*[@id='ul_bestseller_group_category']/li[7]/a"
              }


def trending_call(category, xpath):

    qoo10_url = "https://www.qoo10.sg/gmkt.inc/Bestsellers/?banner_no=12021"

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
        browser.get(qoo10_url)
        browser.implicitly_wait(5)

        #Hover above element
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/header/div[1]/ul/li[2]')))
        hover = ActionChains(browser).move_to_element(element)
        hover.perform()

        #Selecting dropdown
        ship_selector = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='ShipToSelector']")))
        hover = ActionChains(browser).move_to_element(ship_selector)
        hover.click().perform()

        #Selecting region
        region = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layer_major_ship_to']/li[3]")))
        hover = ActionChains(browser).move_to_element(region)
        hover.click().perform()
        sleep(1)

        #Clicking save
        save = browser.find_element_by_xpath(
            "//*[@id='ShipToLangCurrencySelector']/a")
        hover = ActionChains(browser).move_to_element(save)
        hover.click().perform()
        browser.implicitly_wait(3)

        #Selecting category
        item_type = browser.find_element_by_xpath(xpath)
        hover = ActionChains(browser).move_to_element(item_type)
        hover.click().perform()
        sleep(3)

        #Searching for relevant elements
        products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, ".//div[contains(@class,'item')]")))

        #Data Wrangling
        collated = []
        for i in range(10):
            try:
                product = products[i]
                title = product.find_element_by_xpath(
                    ".//a[contains(@class,'tt')]").get_attribute("title")
                price = product.find_element_by_xpath(
                    ".//strong[contains(@title,'Discounted Price')]").text[1:]
                url = product.find_element_by_xpath(
                    ".//a[contains(@class,'tt')]").get_attribute("href")
                img = product.find_element_by_xpath(
                    ".//a[contains(@class,'thmb')]//img").get_attribute("src")
                ratings = "5 stars"
                collated.append([title, price, url, img, ratings])
            except Exception as err:
                raise(err)
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
                "qoo10").child(i+1).set(data)

        browser.quit()

    except Exception as err:
        print(f'Unusual traffic network occured, {err}')
        browser.quit()


for key, value in qoo10_urls.items():
    try:
        trending_call(key, value)
    except:
        continue
