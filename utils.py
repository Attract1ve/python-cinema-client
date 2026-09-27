def parserSearch(response): 
    movies = response["docs"]
    list_of_finding_movie = []
    for num, movie in enumerate(movies, start=1):
        id_movie = movie['id']
        name = movie['name']
        alt_name = movie['alternativeName']
        year = movie['year'] 
        list_of_finding_movie.append({id_movie: f"{num}. {name if name != '' else alt_name} ({year})"})
    return list_of_finding_movie

def parserMovieDetails(response): 
    details = response['docs'][0]
    genres = [genre['name'] for genre in details['genres']]
    return f"""
Название: {details['name'] if details['name'] != '' else details['alternativeName']}
Год: {details['year']}
Рейтинг: {details['ageRating']}
Жанры: {genres}
Рейтинг кинопоиска: {details['rating']['kp']}
Рейтинг IMDB: {details['rating']['imdb']}
Краткое описание: {details['shortDescription']}
        """