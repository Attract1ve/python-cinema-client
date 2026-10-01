import json
from config import HISTORY_PATH
from datetime import datetime

HISTORY_LIST = []

def addToHistoryList(response): 
    details = response['docs'][0]
    search_item = {
        "query": details['name'] if details['name'] != '' else details['alternativeName'],
        "date": datetime.now()
    }
    HISTORY_LIST.append(search_item)    

def saveHistory():
    with open(HISTORY_PATH, "w", encoding="UTF-8") as file: 
        json.dump(HISTORY_LIST, file, indent=4, default=str, ensure_ascii=False)