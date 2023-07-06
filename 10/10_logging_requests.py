import requests
import logging
from http.client import HTTPConnection 

logging.basicConfig()
logging.getLogger("urllib3").setLevel(logging.DEBUG)

# HTTPConnection.debuglevel = 1
result = requests.get("https://msk.rt.ru/")
                             