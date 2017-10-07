import pyautogui
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

req = 'https://coinotron.com/app?action=api&api_key=D4D2C3EB10D94C52A23B1EDF399A7416'

try:
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    d = json.loads(str(page_soup))
    print("Username:", d['username'])
    print("Workers:", d['workers'])

except Exception as e:
    print("Precka!")