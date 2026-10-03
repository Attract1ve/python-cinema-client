import json 
from api import search_movie, get_movie_details
from utils import parser_search, parser_movie_details

response = get_movie_details(885533)
parsed_details = parser_movie_details(response)
print(parsed_details)

# with open("resp.json", "w", encoding="UTF-8") as file:
#     json.dump(response, file, indent=4, ensure_ascii=False)

