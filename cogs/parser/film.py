import requests
from bs4 import BeautifulSoup


class Film():
    def __init__(self, name, film_id, link):
        self.name = name
        self.link = link

        html = get_html(film_id)
        self.mark_kp = self.get_mark_kp(html)
        self.mark_imdb = self.get_mark_imdb(html)

    def get_mark_kp(self, html):
        soup = BeautifulSoup(html, 'lxml')
        mark = soup.find('kp_rating').get_text()
        return mark

    def get_mark_imdb(self, html):
        soup = BeautifulSoup(html, 'lxml')
        mark = soup.find('imdb_rating').get_text()
        return mark

    def get_html(self, film_id):
        return requests.get('https://rating.kinopoisk.ru/'+ film_id + '.xml').content

    def __str__(self):
        return f'{self.name} - {self.mark}'
