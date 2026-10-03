from api import search_movie, get_movie_details
from utils import parser_search, parser_movie_details
from storage import add_to_history_list, save_history, load_history

history_list = load_history()              

command = ""
commands = f"""
    1. Найти фильм
    2. Посмотреть популярные фильмы
    3. История поисков
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
        response = search_movie(name)
        if response is None:
            continue
        movies = parser_search(response)
        movie_ids = []
        for num, movie in enumerate(movies, start=1): 
            print(f"{num}. {movie.get('name')} ({movie.get('year')})")
            movie_ids.append(movie.get('movie_id'))
        
        try:
            num_movie = int(input("Введите номер фильма, или 0, чтобы завершить работу приложения > "))
            if num_movie == 0:
                break
            else: 
                movie_id = movie_ids[num_movie-1]
                response = get_movie_details(movie_id)
                movie_details = parser_movie_details(response)  
                add_to_history_list(history_list, response)
                save_history(history_list)
                print(movie_details)
        except ValueError as e:
            print("Ошибка! Вы ввели не число", e)
        except Exception as e:
            print("Ошибка!!!", e)
    if command == "2": 
        pass
    if command == "3":
        for item in history_list:
            print(f"Запрос: {item['query']}, Дата: {item['date']}")
