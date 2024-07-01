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
finish_time = time.time() + 60

while click_cookie:    
    cookie.click()

    if time.time() > start_time:
        prices = [int(price.text.split("- ")[1].strip().replace(",", "")) for price in driver.find_elements(by=By.CSS_SELECTOR, value="#store b")[:-1]]
        money = int(driver.find_element(By.ID,value="money").text.replace(",", "").replace(" ",""))
        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[prices[n]] = item_ids[n]

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

        start_time = time.time() + 5

    if time.time() > finish_time:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        click_cookie = False

driver.quit()