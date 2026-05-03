from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import smtplib

load_dotenv()

url = 'https://appbrewery.github.io/instant_pot/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name='span', class_='aok-offscreen').getText()
price_text = price.split('$')[1]
price_float = float(price_text)
print(price_float)


title = soup.find(id='productTitle').getText().strip()
print(title)

BUY_PRICE = 100

if price_float < BUY_PRICE:
    message = f'{title} is on sale for {price}!'

    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_ADDRESS'],
            msg=f'Subject:Amazon Price Alert\n\n{message}\n{url}'.encode('utf-8')
        )