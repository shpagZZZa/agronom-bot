import json
import random


class FilmGetter:
    def __init__(self):
        films = FilmGetter.get_films()
        self.film = random.choice(films)

    @staticmethod
    def get_films():
        with open('films.txt') as file:
            films = json.load(file)
        return films


