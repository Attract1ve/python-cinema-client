import json
from config import HISTORY_PATH
from datetime import datetime


def add_to_history_list(history_list, response): 
    details = response.get('docs', [{}])[0]
    search_item = {
        "query": details.get('alternativeName', 'неизвестно'),
        "date": datetime.now()
    }
    history_list.append(search_item)    

def save_history(history_list):
    with open(HISTORY_PATH, "w", encoding="UTF-8") as file: 
        json.dump(history_list, file, indent=4, default=str, ensure_ascii=False)

def load_history():
    try:
        with open(HISTORY_PATH, "r", encoding="UTF-8") as file: 
            history = json.load(file)
            return history
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Ошибка при загрузке истории: {e}")
        return []