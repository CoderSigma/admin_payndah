import requests
from termcolor import colored
from colorama import Fore
import colorama
from tqdm import tqdm
import argparse
import threading
import time
import datetime

colorama.init()

def logo():
    print(Fore.RED+"""
░█▀▀█ █▀▀▄ █▀▄▀█ ░▀░ █▀▀▄ 　 █▀▀ ░▀░ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ 
▒█▄▄█ █░░█ █░▀░█ ▀█▀ █░░█ 　 █▀▀ ▀█▀ █░░█ █░░█ █▀▀ █▄▄▀ 
▒█░▒█ ▀▀▀░ ▀░░░▀ ▀▀▀ ▀░░▀ 　 ▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀
                                             by : Coder Sigma 

command = adm.py -u <site> then wait for the results
""")    
wordlist = open("list.txt","r")
def findPanel(url):
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+"/"+words)
        if req.status_code == 200:
            print(req.url)
parser = argparse.ArgumentParser("""
python3 AdminFinder -u [url]
ex:python3 AdminFinder -u http://site.com
""")
parser.add_argument("-u","--url")
args = parser.parse_args()
urls = args.url
if urls !=None:
    for _ in tqdm(range(5),
                  desc="Loading...",
                  ascii=False, ncols=75):
        time.sleep(0.3) #loading...
    for i in range(50):
        url = threading.Thread(target=findPanel,args=(urls,))
        url.start()
else:
    logo()


logo()
