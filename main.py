import requests
from config import API_TOKEN, BASE_URL
import json
from api import searchFilm
from utils import parser
headers = {
        "X-API-KEY": API_TOKEN
}
