from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://ozh.github.io/cookieclicker/')

sleep(2)

language = driver.find_element(By.ID, value='langSelect-EN')
language.click()

sleep(2)

cookie = driver.find_element(By.ID, value='bigCookie')
items = [f'product{i}' for i in range(18)]


while True: 
    cookie.click()
    cookie_text = driver.find_element(by=By.ID, value="cookies").text
    cookie_count = int(cookie_text.split()[0].replace(",", ""))
    if cookie_count % 50 == 0:
        for product in reversed(items):
            try:
                best_item = driver.find_element(By.ID, value=product)
                print(best_item)
                element_class = best_item.get_attribute('class').split()[2]
            except:
                cookie.click()
            else: 
                if element_class == 'enabled':
                    best_item.click()
                    break
