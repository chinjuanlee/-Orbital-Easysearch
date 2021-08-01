from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import pyrebase
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

def crawl(keyword, number):
    #Website URL
     amazon_url = f"https://www.amazon.sg/s?k={keyword}&ref=nb_sb_noss"

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

     if number == 3:
        return "Task not complete"

     try:
        #Chrome Options
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument('headless') 
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")

        #Initialising ChromeDriver
        browser = webdriver.Chrome(options = options, executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        browser.get(amazon_url)

        #Hover and click country
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nav-global-location-popover-link"]')))  
        hover = ActionChains(browser).move_to_element(element)
        hover.click().perform()                        

        #Changing regional address
        input_postal_code = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, './/input[contains(@data-action, "GLUXPostalInputAction")]')))   
        input_postal_code.send_keys("180001")
        
        #Click apply button
        apply_btn = browser.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input')
        hover = ActionChains(browser).move_to_element(apply_btn)
        hover.click_and_hold().perform()
        sleep(1)
        hover.release().perform()
        sleep(3)

        #Searching for relevant elements
        products = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.XPATH, ".//div[contains(@class,'a-section a-spacing-medium')]")))
                
        #Data Wrangling
        collated = []
        if len(products) > 10:
            search_num = 10
        else:
            search_num = len(products)

        for i in range(search_num):
            try:
                product = products[i]
                title = product.find_element_by_xpath(".//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]").text
                url = product.find_element_by_xpath(".//a[contains(@class,'a-link-normal a-text-normal')]").get_attribute('href')
                img = product.find_element_by_xpath(".//img[contains(@class,'s-image')]").get_attribute('src')
                price_whole = product.find_element_by_xpath(".//span[contains(@class,'a-price-whole')]").text
                price_fraction = product.find_element_by_xpath(".//span[contains(@class,'a-price-fraction')]").text
                price = formatter(f"${price_whole}.{price_fraction}") 
                review_bar = product.find_element_by_xpath(".//div[contains(@class, 'a-section a-spacing-none a-spacing-top-micro')]")
                review = formatter(review_bar.find_element_by_xpath(".//span[contains(@class, 'a-size-base')]").text)
                ratings =  product.find_element_by_xpath(".//div[contains(@class, 'a-row a-size-small')]/span").get_attribute('aria-label')
                ratings = f'{float(ratings[:3])} stars'
                collated.append([title, price, url, review, img, ratings])
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
   
        sorted_collated = sorted(collated_updated, key = lambda x : float(x[1][1:]), reverse = True)       
        sorted_collated = sorted(sorted_collated, key = lambda x : int(x[3]), reverse = True)[:3]
        
        #Handling for results with less than 3 products
        for i in range(3 - len(sorted_collated)):
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

        return "Task completed"

     except Exception as err:
        print(browser.page_source)
        browser.quit()
        print("trigger")
        return crawl(keyword, number + 1)

def formatter(str_input):
    formatted = ""
    for char in str_input:
        if not char == ",":
            formatted += char
    return formatted

