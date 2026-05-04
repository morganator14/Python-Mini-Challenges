from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
submit = driver.find_element(By.CLASS_NAME, value='btn')

fname.send_keys('Morgan')
lname.send_keys('Morgan')
email.send_keys('hello@gmail.com')
submit.click()