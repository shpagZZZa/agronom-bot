import requests
import random
import json
from film import *
from bs4 import BeautifulSoup
from lxml import etree

class KinopoiskParser():
    def __init__(self, url):
        self.url = url

    def get_html(self):
        return requests.get(self.url).content

    def get_random_film(self, films):
        return random.choice(films)

    def get_table(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        return soup.find_all('table', {
                'cellspacing' : '0',
                'cellpadding' :'3',
                'width': '100%',
                'border': '0',
                'class': '',
            })[0]

    def parse_table(self, table):
        soup = BeautifulSoup(table.prettify(), 'lxml')
        films = []
        for row in soup.find_all('tr')[1:]:
            film = self.get_film(row)
            films.append(film)
        return films
            

    def get_film(self, row):
        soup = BeautifulSoup(row.prettify(), 'lxml')
        info = soup.find(attrs={'class': 'all'})
        href = info['href']
        
        name = info.get_text()
        film_id = href.split('/')[2]
        link = 'https://www.kinopoisk.ru' + href
        return Film(name, film_id, link)
        

    def get_films(self, urls):
        pass
        films = []
        for url in urls:
            films.append(Film(url))
        return films




url = 'https://www.kinopoisk.ru/top/asc/1/'
parser = KinopoiskParser(url)
table = parser.get_table()
films = parser.parse_table(table)
for film in films:
    print(film)
