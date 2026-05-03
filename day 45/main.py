from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com/')

yc = response.text

soup = BeautifulSoup(yc, 'html.parser')
article_tag = soup.find_all(name='a', class_='storylink')
article_text = []
article_link = []

for article in article_tag:
    text = article.getText()
    article_text.append(text)
    link = article.get('href')
    article_link.append(link)
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_upvote)

largest = max(article_upvote)
largest_index = article_upvote.index(largest)
print(len(article_text))
print(largest_index)
print(article_text[largest_index])
print(article_tag[largest_index])

