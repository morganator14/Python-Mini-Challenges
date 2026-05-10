from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = os.getenv('TWITTER_EMAIL')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.testmyspeed.com/")
        go_btn = self.driver.find_element(By.CSS_SELECTOR, value=".go-button")
        go_btn.click()
        
        wait = WebDriverWait(self.driver, 60)
        upload = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="tms-root"]/div/div/section/div[1]/section[1]/div[2]/section[1]/div[3]/div[1]/span[2]/span[1]')))
        download = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="tms-root"]/div/div/section/div[1]/section[1]/div[2]/section[1]/div[2]/div[1]/span[2]/span[1]')))

        self.up = upload.text
        self.down = download.text
        print(self.up, self.down)


    def tweet_at_provider(self):
        self.driver.get("https://x.com")
        wait = WebDriverWait(self.driver, 5)

        login_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div/div/div[3]/div[4]/a')))
        login_btn.click()

        email_field = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        email_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        email_field.send_keys(TWITTER_EMAIL)
        email_next.click()

        password_field = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div/input')))
        password_next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        password_field.send_keys(TWITTER_PASSWORD)
        password_next.click()

        compose = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        tweet = f'Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'
        compose.send_keys(tweet)

        post_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/button')
        post_btn.click()

        self.driver.quit()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()


