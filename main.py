import requests
from config import API_TOKEN, BASE_URL
import json
from api import searchFilm, getMovieDetails
from utils import parserSearch, parserMovieDetails

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
        movies = parserSearch(response)
        movie_ids = []
        for movie in movies: 
            for key, value in movie.items():
                print(value)
                movie_ids.append(key)
        print("Если вы хотите узнать подробную информацию об фильме")
        try:
            num_movie = int(input("Введите номер фильма, или 0, если не хотите > "))
            if num_movie == 0:
                continue
            else: 
                movie_id = movie_ids[num_movie-1]
                response = getMovieDetails(movie_id)
                movie_details = parserMovieDetails(response)
                print(movie_details)
        except ValueError as e:
            print("Ошибка! Вы ввели не число", e)
        except Exception as e:
            print("Ошибка!!!", e)
    if command == "3":
        pass 
    if command == 4:
        pass
        