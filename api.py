import requests
import json
from config import API_TOKEN, BASE_URL, HEADERS

def searchFilm(name): 
    params = {
        "query": name,
    }
    try: 
        response = requests.get(f"{BASE_URL}/search", headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e: 
        print(f"HTTP ошибка: {e}")
        print(f"Статус: {response.status_code}")
    except requests.ConnectionError as e:
        print(f"Ошибка соеденения: {e}")
    except requests.Timeout as e: 
        print(f"Таймаут: {e}")
    except requests.RequestException as e: 
        print(f"Другая ошибка requests: {e}")
     
def getMovieDetails(movie_id): 
    params = {
        "id": movie_id
    }
    try: 
        response = requests.get(f"{BASE_URL}", headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e: 
        print(f"HTTP ошибка: {e}")
        print(f"Статус: {response.status_code}")
    except requests.ConnectionError as e:
        print(f"Ошибка соеденения: {e}")
    except requests.Timeout as e: 
        print(f"Таймаут: {e}")
    except requests.RequestException as e: 
        print(f"Другая ошибка requests: {e}")
        
def randomMovie(): 
    try: 
        response = requests.get(f"{BASE_URL}/random", headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e: 
        print(f"HTTP ошибка: {e}")
        print(f"Статус ошибки: {response.status_code}")
    except requests.ConnectionError as e:
        print(f"Ошибка соеденения: {e}")
    except requests.Timeout as e: 
        print(f"Таймаут: {e}")
    except requests.RequestException as e:
        print(f"Другая ошибка requests: {e}")
        