from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a')
#article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
#all_portals.click()

search = driver.find_element(By.CLASS_NAME, value='mw-ui-icon-search')
search.click()
searchbar = driver.find_element(By.NAME, value='search')
searchbar.send_keys("Python", Keys.ENTER)
