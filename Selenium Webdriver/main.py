from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.python.org/")

#price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
#price_cents = driver.find_element(By.CLASS_NAME, value-'a-price-fraction')

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(link)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# driver.close()

dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery ul li time')
titles = driver.find_elements(By.CSS_SELECTOR, value='.event-widget .shrubbery ul li a')

titles = [title.text for title in titles]
days = [date.get_attribute('datetime').split('T') for date in dates]

event_dict = {i: {'time': date[0], 'title': title} for i, (date, title) in enumerate(zip(days,titles))}
print(event_dict)
driver.close()