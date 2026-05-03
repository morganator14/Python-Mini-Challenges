from bs4 import BeautifulSoup
import requests

url = 'https://appbrewery.github.io/instant_pot/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
price = soup.find(name='span', class_='aok-offscreen').getText()
price_text = price.split('$')[1]
price_float = float(price_text)
print(price_float)