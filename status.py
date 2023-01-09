import requests
import time
from itertools import cycle
import random

tokenzyy = "your token here"

def okda(token):
    tokenzy = {"authorization":f"{tokenzyy}"}
    statuses = cycle(["online", "idle", "dnd"]) #add "invisible" if you want to roll with it too
    while True:
        settings = {
        'status': next(statuses)
        }
        while True:
            try:
                time.sleep(2)
                e = requests.patch("https://discord.com/api/v8/users/@me/settings", headers = tokenzy, json = settings)
                print(e)
            except Exception:
                break
            else:
                break
okda(tokenzyy)




            
