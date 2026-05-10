from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import smtplib

load_dotenv()

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
response = requests.get(url, 
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"})

soup = BeautifulSoup(response.text, 'html.parser')
price_whole = soup.find(name='span', class_='a-price-whole').getText()
price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
price = price_whole + price_fraction
price = float(price)


title = soup.find(id='productTitle').getText().strip()
print(title)

BUY_PRICE = 200

if price < BUY_PRICE:
    message = f'{title} is on sale for {price}!'

    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_ADDRESS'],
            msg=f'Subject:Amazon Price Alert\n\n{message}\n{url}'.encode('utf-8')
        )