from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

webpage = response.text

soup = BeautifulSoup(webpage,'html.parser')
film = soup.find_all(name='h3',class_='title')
films = []
for f in film:
    text = f.getText()
    films.append(text)

films = films.reverse()

with open('movies.txt', mode='w') as file:
    for movie in films:
        file.write(f"{movie}\n")