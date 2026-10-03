import requests
from config import BASE_URL, HEADERS


def make_request(url, params=None): 
    try:
        response = requests.get(
            url=url, 
            headers=HEADERS,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e: 
        print(f"HTTP ошибка: {e}")
    except requests.ConnectionError as e:
        print(f"Ошибка соеденения: {e}") 
    except requests.Timeout as e:
        print(f"Таймаут: {e}")
    except requests.RequestException as e: 
        print(f"Ошибка: {e}")
        

def search_movie(name): 
    params = {
        "query": name,
    }
    return make_request(
        url=f"{BASE_URL}/search", 
        params=params
    )
     
def get_movie_details(movie_id): 
    params = {
        "id": movie_id
    }
    
    return make_request(
        url=f"{BASE_URL}", 
        params=params
    )
        
def random_movie(): 
    return make_request(
        url=f"{BASE_URL}/random"
    )