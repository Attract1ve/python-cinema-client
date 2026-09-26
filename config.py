import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "https://api.poiskkino.dev/v1.5/movie"