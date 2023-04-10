import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("dsjkjkds")
except InvalidURL:
    print("invalid url was given")