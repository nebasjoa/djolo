import pyautogui
import socket
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

if __name__ == '__main__':
    while True:
        try:
            req = 'https://dwarfpool.com/eth/address?wallet=23d7126b2200090aff5a4eb42fa1e5611c2d4314'
            paket_list = []
            uClient = uReq(req)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            table = page_soup.findAll("table", {"class": "table no-bottom-margin table-striped table-condensed"})
            i = -1
            for row in table[1].findAll("tr"):
                i += 1
                cells = row.findAll("td")
                if len(cells) > 0:
                    miner = cells[0].text.strip()
                    sent_hash = int(float(cells[2].text.strip()))
                    print(sent_hash)
                    #if provera da li je sent_hash 0, ako jeste, racunar se restartuje
                    if sent_hash < 200: # == 0 ili 10
                        #za restart racunara se koristi PYAUTOGUI modul koji simulira klik misa ili unos preko tastature
                        print("Miner broj " + str(i) + " manji od 200")
                        pyautogui.click(x = 0, y = 1080, interval=2)
            time.sleep(5)
        except socket.error as e:
            print("No Internet connection!")
