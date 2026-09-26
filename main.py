import requests
from config import API_TOKEN, BASE_URL
import json
from api import searchFilm
from utils import parser

command = ""
commands = f"""
    1. Найти фильм
    2. Посмотреть популярные фильмы
    3. Случайный фильм
    4. История поисков
    0. Выход 
    -1. посмотреть список комманд
"""

print(commands)
while command != "0": 
    command = input("Введите номер команды > ")
    if command == "-1":
        print(commands)
    if command == "1": 
        name = input("Введите название фильма > ")
        response = searchFilm(name)
        movies = parser(response)
        movie_ids = []
        for movie in movies: 
            for key, value in movie.items():
                print(value)
                movie_ids.append(key)
        print("Если вы хотите узнать подробную информацию об фильме")
        num_movie = input("Введите номер фильма > ")
        