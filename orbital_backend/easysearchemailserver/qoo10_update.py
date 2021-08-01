from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import update
import os

def check(dict_item):
    title = dict_item["title"]
    ratings = dict_item["ratings"]
    img = dict_item["image"]
    qoo10_url = dict_item["url"]
    price_initial = dict_item["price"]
    keyword = dict_item["item"]

    try:
        #Chrome Options
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument('headless') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")

        #Initialising ChromeDriver
        browser = webdriver.Chrome(options = options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        browser.get(qoo10_url)
        sleep(3)

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
        sleep(3)

        try:
            price = browser.find_element_by_xpath('//*[@id="discount_info"]/dl[1]/dd/strong').text[1:]

        except Exception as err:
            price = browser.find_element_by_xpath('//*[@id="qprice_span"]').text[1:]

        browser.quit()

        if float(price[1:]) >= float(price_initial[1:]):
            print("Higher/Same")
            update.realtime(
                [keyword, [title, price, qoo10_url, img, ratings], "qoo10"])
            dict_output = dict_item.copy()
            dict_output["price"] = price
            return dict_output
        else:
            print("Lower")
            update.realtime(
                [keyword, [title, price, qoo10_url, img, ratings], "qoo10"])
            dict_output = dict_item.copy()
            dict_output["price"] = price
            return dict_output

    except Exception as err:
        print(f"Error, {err}")
        return dict_item


def formatter(str_input):
    formatted = ""
    for char in str_input:
        if not char == ",":
            formatted += char
    return formatted


#Testing
test_dict = {'image': 'https://gd.image-gmkt.com/li/521/441/1628441521.g_100-w-st_g.jpg',
             'item': 'airpods',
             'price': '$145.00',
             'ratings': '5 stars',
             'store': 'qoo10',
             'url': 'https://www.qoo10.sg/item/AIRPODS-SG-APPLE-WARRANTY-APPLE-AIRPODS-GEN-2-WIRELESS-BLUETOOTH-EARPHONES/611727018?banner_no=1305330',
             'title': '**SG Apple Warranty** ★ Apple AirPods Gen 2 Wireless Bluetooth Earphones ★ Genuine Apple'}

