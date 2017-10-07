# instaliraj python3.x
# instaliraj pip!!!
# dodaj python u PATH (environment variables)
import pyautogui #pip
import datetime
import socket
import time
from urllib.request import urlopen as uReq #urlib pip
from bs4 import BeautifulSoup as soup #pip

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
            for row in table[1].findAll("tr"): #from HTML table find all rows
                cells = row.findAll("td") #from row find all cells
                if len(cells) > 0:
                    miner = cells[0].text.strip()
                    sent_hash = int(float(cells[2].text.strip()))
                    paket = [sent_hash]
                    paket_list.append(paket)
            a = str(paket_list[0]) # prvi miner iz dwarf tabele 1. CA
            b = a[1] + a[2]
            print("Sent hashrate MINER 1.: " + b + " MHs" + " - Date and time: " + "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()))
            int_sent = int(b)

            #if provera da li je sent_hash 0, ako jeste, racunar se restartuje
            if int_sent < 200: # Sent hashrate manji od 10 MHs
                #za restart racunara se koristi PYAUTOGUI modul koji simulira klik misa ili unos preko tastature
                #Start -> Strelica pored Shut down -> Restart
                print("Hashrate less than 200 MHs, restarting...")
                pyautogui.click(x=0, y=1080, interval=2)
                pyautogui.moveTo(x=355, y=1005)
                pyautogui.moveTo(x=355, y=1005, duration=1)
                pyautogui.moveTo(x=380, y=965, duration=1) # promeniti moveTo na click
            time.sleep(600) #na koliko sekundi ce se izvrsavati skripta

        except socket.error as e:
            print("No Internet connection!")

#.bat staviti u Startup folder
