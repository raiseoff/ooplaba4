from pathlib import Path
from datetime import timedelta
from dotenv import dotenv_values
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
ENV = dotenv_values(str(BASE_DIR) + "/env.env")
print(ENV)