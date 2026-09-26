def parser(response_dict): 
    movies = response_dict["docs"]
    list_of_finding_movie = []
    for num, movie in enumerate(movies, start=1):
        id_movie = movie['id']
        name = movie['name']
        alt_name = movie['alternativeName']
        year = movie['year'] 
        list_of_finding_movie.append({id_movie: f"{num}. {name if name != '' else alt_name} ({year})"})
    return list_of_finding_movie

