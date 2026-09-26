def parser(response_dict): 
    movies = response_dict["docs"]
    list_of_finding_movie = []
    for num, movie in enumerate(movies, start=1): 
        list_of_finding_movie.append(f"{num}. {movie['name'] if movie['name'] != '' else movie['alternativeName']} ({movie['year']})")
    return list_of_finding_movie

