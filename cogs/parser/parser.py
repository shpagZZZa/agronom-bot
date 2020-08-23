import requests
import random
import json
from film import Film
from bs4 import BeautifulSoup


class KinopoiskParser:
    def __init__(self, url):
        self.url = url
        self.films = self.get_films()

    def write_json(self):
        with open('../films.txt', 'w') as file:
            file.truncate()
            json.dump(self.films, file)

    def get_html(self):
        return requests.get(self.url).content

    def get_table(self):
        soup = BeautifulSoup(self.get_html(), 'lxml')
        return soup.find_all('table', {
            'cellspacing': '0',
            'cellpadding': '3',
            'width': '100%',
            'border': '0',
            'class': '',
        })[0]

    def get_films(self):
        table = self.get_table()
        soup = BeautifulSoup(table.prettify(), 'lxml')
        films = []
        for row in soup.find_all('tr')[1:]:
            film = self.get_film(row).to_json()
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

#
url = 'https://www.kinopoisk.ru/top/asc/1/'
parser = KinopoiskParser(url)
parser.write_json()
