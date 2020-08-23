import requests
from bs4 import BeautifulSoup
import json


class Film:
    def __init__(self, name, film_id, link):
        self.name = name.replace('\n', '')
        self.link = link
        self.film_id = film_id

        html = self.get_html(film_id)
        self.mark_kp = self.get_mark_kp(html)

    def get_mark_kp(self, html):
        soup = BeautifulSoup(html, 'lxml')
        mark = soup.find('kp_rating').get_text()
        return mark

    def get_mark_imdb(self, html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            mark = soup.find('imdb_rating').get_text()
            return mark
        except:
            print(f'{self.name} has no imdb rating')

    def get_html(self, film_id):
        return requests.get('https://rating.kinopoisk.ru/' + str(film_id) + '.xml').content

    def to_json(self):
        return {
            'name': self.name,
            'rating': self.mark_kp,
            'link': self.link
        }