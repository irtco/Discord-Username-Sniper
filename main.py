import requests
import json
from pystyle import *
import time
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Username Sniper | Made by: irtco#0702")

with open('config.json', 'r') as c:
    config = json.load(c)
    TOKEN = config["TOKEN"]
    PASSWORD = config["PASSWORD"]
    TAG = config["TAG"]
    USERNAME = config["USERNAME"]



url = "https://discord.com/api/v9/users/@me"

header ={
    "authorization": TOKEN
}

payload = {
    "discriminator": TAG,
    "password": PASSWORD,
    "username": USERNAME,
}





title = f"""
    ____  _                          __          
   / __ \(_)_____________  _________/ /          
  / / / / / ___/ ___/ __ \/ ___/ __  /           
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /            
/_____/_/____/\___/\____/_/   \__,_/             
  / / / /_______  _________  ____ _____ ___  ___ 
 / / / / ___/ _ \/ ___/ __ \/ __ `/ __ `__ \/ _ \\
/ /_/ (__  )  __/ /  / / / / /_/ / / / / / /  __/
\____/____/\___/_/  /_/ /_/\__,_/_/ /_/ /_/\___/ 
  / ___/____  (_)___  ___  _____                 
  \__ \/ __ \/ / __ \/ _ \/ ___/                 
 ___/ / / / / / /_/ /  __/ /                     
/____/_/ /_/_/ .___/\___/_/                      
            /_/       

Username To Snipe: {USERNAME}
Tag To Snipe: {TAG}

Press ENTER To Start
"""

sniped = """
            .-""-.
           / .--. \\
          / /    \ \\         _____       _                __
          | |    | |        / ___/____  (_)___  ___  ____/ /
          | |.-""-.|        \__ \/ __ \/ / __ \/ _ \/ __  / 
         ///`.::::.`\\      ___/ / / / / / /_/ /  __/ /_/ /  
        ||| ::/  \:: ;    /____/_/ /_/_/ .___/\___/\__,_/   
        ||; ::\__/:: ;                /_/                   
         \\\\\ '::::' /
          `=':-..-'`
"""

System.Size(200,40)

Anime.Fade(Center.Center(title), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)

atp = 0

print(Colorate.Horizontal(Colors.blue_to_purple, title, 1))
print(Colorate.Horizontal(Colors.purple_to_blue, "[+] Sniping...", 1))
def sniper():
    global atp
    r = requests.patch(url=url,headers=header,json=payload)
    atp += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Username Sniper | Attempts:{atp}")
    if r.status_code == 200:
        Anime.Fade(Center.Center(sniped), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)
        
i=1
while i<5:
    sniper()

