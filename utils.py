def parser_search(response): 
    movies = response.get('docs', [])
    list_of_finding_movie = []
    for movie in movies:
        name = movie.get('name', "неизвестно")
        alt_name = movie.get('alternativeName', "неизвестно")
        movie_info = {
            "movie_id": movie.get('id', 'неизвестно '),
            "name": name if name != "" else alt_name, 
            "year": movie.get('year', 'неизвестно')     
        }
        list_of_finding_movie.append(movie_info)
    return list_of_finding_movie

def parser_movie_details(response): 
    details = response.get('docs', [{}])[0]
    genres = [genre.get('name') for genre in details.get('genres', [])]
    return f"""
Название: {details.get('alternativeName', 'неизвестно')}
Год: {details.get('year', 'неизвестно')}
Рейтинг: {details.get('ageRating', 'неизвестно')}
Жанры: {genres}
Рейтинг кинопоиска: {details.get('rating', {}).get('kp', 'неизвестно')}
Рейтинг IMDB: {details.get('rating', {}).get('imdb', 'неизвестно')}
Краткое описание: {details.get('shortDescription', 'неизвестно')}
        """
        