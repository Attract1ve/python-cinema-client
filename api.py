import requests
import json
from config import API_TOKEN, BASE_URL

def searchFilm(name): 
    params = {
        "query": name,
    }
    headers = {
        "X-API-KEY": API_TOKEN
    }
    try: 
        response = requests.get(f"{BASE_URL}/search", headers=headers, params=params, timeout=5)
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
     
