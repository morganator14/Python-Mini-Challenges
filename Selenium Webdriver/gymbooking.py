from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException
from time import time
import os


EMAIL = 'student@test.com'
PASSWORD = 'password123'
GYM_URL = 'https://appbrewery.github.io/gym/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver,2)

login_btn = wait.until(ec.element_to_be_clickable((By.ID,'login-button')))
login_btn.click()

email_input = wait.until(ec.presence_of_element_located((By.ID, 'email-input')))
password_input = driver.find_element(By.ID, value='password-input')

email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)

for attempt in range(3):
    try:
        submit_btn = driver.find_element(By.ID, "submit-button")
        submit_btn.click()
        break
    except StaleElementReferenceException:
        time.sleep(0.5)

tuesday = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[contains(@id, 'tue')]//button[contains(@id, '1800')]")
    )
)

thursday = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[contains(@id, 'thu')]//button[contains(@id, '1800')]")
    )
)

tue_class_type = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[contains(@id, 'tue')]//h3[contains(@id, 'class-name-') and contains(@id, '1800')]")
    )
    ).text

tue_date = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(@id, 'tue')]")
    )
).text
tue_class_date = tue_date[5:]

thu_class_type = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//div[contains(@id, 'thu')]//h3[contains(@id, 'class-name-') and contains(@id, '1800')]")
    )
    ).text

thu_date = wait.until(
    ec.presence_of_element_located(
        (By.XPATH, "//h2[contains(@id, 'thu')]")
    )
).text
thu_class_date = thu_date[5:]

classes_booked = 0
waitlists_joined = 0
already_booked = 0
tuethu_classes = 0
new_booking = ''
booking_date = ''
new_waitlist = ''
waitlist_date = ''

class_buttons = driver.find_elements(By.XPATH, value="//button[contains(@id, 'book-button')]")

for button in class_buttons:
    if button == tuesday:
        if tuesday.text == "Booked":
            print(f'You already booked {tue_class_type} on {tue_class_date}!')
            already_booked += 1

        elif tuesday.text == "Waitlisted":
            print(f'Class is currently full, you are on the waitlist for {tue_class_type} on {tue_class_date}.')
            already_booked += 1

        elif tuesday.text == "Join Waitlist":
            tuesday.click()
            print(f'You have joined the waitlist for {tue_class_type} on {tue_class_date}!')
            waitlists_joined += 1
            new_waitlist = tue_class_type
            waitlist_date = tue_class_date

        else:
            tuesday.click()
            print(f'Booked: {tue_class_type} on {tue_class_date}, see you then!')
            classes_booked += 1
            tuethu_classes += 1
            new_booking = tue_class_type
            booking_date = tue_class_date

    elif button == thursday:
        if thursday.text == "Booked":
            print(f'You already booked {thu_class_type} on {thu_class_date}!')
            already_booked += 1

        elif thursday.text == "Waitlisted":
            print(f'Class is currently full, you are on the waitlist for {thu_class_type} on {thu_class_date}.')
            already_booked += 1

        elif thursday.text == "Join Waitlist":
            thursday.click()
            print(f'You have joined the waitlist for {thu_class_type} on {thu_class_date}!')
            waitlists_joined += 1
            if new_waitlist == thu_class_type:
                waitlist_date += 'and' + thu_class_date
            else:
                new_waitlist += 'and' + thu_class_type
                waitlist_date += 'and' + thu_class_date

        else:
            thursday.click()
            print(f'Booked: {thu_class_type} on {thu_class_date}, see you then!')
            classes_booked += 1
            tuethu_classes += 1
            if new_booking == thu_class_type:
                booking_date += 'and' + thu_class_date
            elif new_booking == '':
                new_booking = thu_class_type
                booking_date = thu_class_date
            else:
                new_booking += 'and' + thu_class_type
                booking_date += 'and' + thu_class_date

print(f'---Booking Summary---\n' \
f'Classes booked: {classes_booked}\n' \
f'Waitlists joined: {waitlists_joined}\n' \
f'Already booked: {already_booked}\n' \
f'Total Tuesday and Thursday 6pm classes processed: {tuethu_classes}')

if classes_booked != 0:
    print(f'---Detailed Class List---\n'
        f'[New Booking] {new_booking} on {booking_date}')


elif waitlists_joined != 0:
    print(f'[New Waitlist] {new_waitlist} on {waitlist_date}')