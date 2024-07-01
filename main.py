from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

import time

start_time = time.time() + 5

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,value="cookie")
click_cookie = True
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
five_min = time.time() + 60*5



while click_cookie:    
    cookie.click()

    if time.time() > start_time:
        prices = [int(price.text.split("- ")[1].strip().replace(",", "")) for price in driver.find_elements(by=By.CSS_SELECTOR, value="#store b")[:-1]]
        money = int(driver.find_element(By.ID,value="money").text.replace(",", ""))
    cookie_upgrades = {}
    for n in range(len(prices)):
        cookie_upgrades[prices[n]] = item_ids[n]



driver.quit()