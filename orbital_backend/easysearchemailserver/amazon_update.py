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
    amazon_url = dict_item["url"]
    price_initial = dict_item["price"]
    keyword = dict_item["item"]
    if dict_item['item'] != "trending":
        url = f"https://www.amazon.sg/s?k={keyword}&ref=nb_sb_noss"
    else:
        url = amazon_url

    userAgent = "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11"

    try:
        #Chrome Options
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument('headless') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent={userAgent}")

        #Initialising ChromeDriver
        browser = webdriver.Chrome(options = options, executable_path=os.environ.get("CHROMEDRIVER_PATH")) 
        browser.get(url)
        sleep(3)
        
        #Hover and click country
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nav-global-location-popover-link"]')))
        hover = ActionChains(browser).move_to_element(element)
        hover.click().perform()

        #Changing regional address
        input_postal_code = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, './/input[contains(@data-action, "GLUXPostalInputAction")]')))
        input_postal_code.send_keys("068623")

        #Click apply button
        apply_btn = browser.find_element_by_xpath(
            '//*[@id="GLUXZipUpdate"]/span/input')
        hover = ActionChains(browser).move_to_element(apply_btn)
        hover.click_and_hold().perform()
        browser.implicitly_wait(1)
        hover.release().perform()
        sleep(3)

        if dict_item['item'] == "trending": 
            price = formatter(browser.find_element_by_xpath(
                ".//span[contains(@id,'priceblock_ourprice')]").text[1:])
        else:
            products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, ".//div[contains(@class,'a-section a-spacing-medium')]")))
            sleep(3)
            for i in range(len(products)):
                product = products[i]
                print(product)
                try:
                    title_updated = product.find_element_by_xpath(".//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]").text
                except:
                    continue
                if title == title_updated:
                    price_whole = product.find_element_by_xpath(".//span[contains(@class,'a-price-whole')]").text
                    price_fraction = product.find_element_by_xpath(".//span[contains(@class,'a-price-fraction')]").text
                    price = formatter(f"${price_whole}.{price_fraction}") 
                    break

        browser.quit()

        if float(price[1:]) >= float(price_initial[1:]):
            print("Higher/Same")
            update.realtime(
                [keyword, [title, price, amazon_url, img, ratings], "amazon"])
            dict_output = dict_item.copy()
            dict_output["price"] = price 
            return dict_item
        else:
            print("Lower")
            update.realtime(
                [keyword, [title, price, amazon_url, img, ratings], "amazon"])
            dict_output = dict_item.copy()
            dict_output["price"] = price
            return dict_output

    except Exception as err:
        print(f"Error/Not found, {err}")
        return dict_item


def formatter(str_input):
    formatted = ""
    for char in str_input:
        if not char == ",":
            formatted += char
    return formatted


#Testing
test_dict = {'price': '$6.95',
             'image': 'https://m.media-amazon.com/images/I/71Gc4RvxEUL._AC_UL320_.jpg',
             'title': 'Serious Foods Popcorn Multipack, Sweet and Salty, 120 g',
             'url': 'https://www.amazon.sg/Serious-Foods-Popcorn-Multipack-Sweet/dp/B07L8NVH5Z/ref=sr_1_7?dchild=1&keywords=popcorn&qid=1624548789&refresh=1&sr=8-7',
             'store': 'amazon',
             'item': 'popcorn',
             'ratings': '4.4 stars'}

#print(check(test_dict))
