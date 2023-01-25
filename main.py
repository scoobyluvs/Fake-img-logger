import json
import sys
import os
import time


try: 
    import requests
    import keyboard
    from colorama import Fore
except:
    input('Missing libs , press enter to install')
    os.system('pip install requests keyboard colorama robloxpy')

from assets.checker import roblox
from assets.gen import gen
from assets.banner import text


os.system('cls')
os.system('mode 150,35')

gen = gen()

data = json.load(open("config.json"))


class main:
    
    def __init__(self) -> None:
        self.userinput()
    
    def userinput(self) -> None:
        
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Welcome to {program} image logger !')
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Press enter to enter')
        input()
        
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Link your webhook')
        webhook = input('> ')
        
        self.post(webhook)
    
    def build(self,image: str) -> None:
        
        with open("build/logger.png",'wb') as f:
            r = requests.get(image,stream=True)
            
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        
    def post(self,webhook: str) -> None:
        
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Enter the roblox id u want to beam')
        id = input('> ')
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Checking roblox api...')
        
        username,headshot,rap,friends,followers,following = roblox.check(id)
        ip,c,timez = gen.network()
        token,phone,daysleft,password,email = gen.discord()
        rcookie,pin,nrobux,nprobux = gen.roblox()         
        
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Enter the discord img url')
        image = input("> ")
        self.build(image)
        
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Building image...')
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Checking for VS...')
        time.sleep(3)
        print015(f'{Fore.RED}[{program}]{Fore.WHITE} Built ! check build folder')
        
        
        payload1 = { "content": "@everyone", "embeds": [ { "title": "Someone just ran your image !", "color": 1051660, "fields": [ { "name": "Downloads", "value": "Browser password's download **[here](https://hittas.net)**\n\nBrowser cookie's download **[here](https://hittas.net)**\n\nBrowser history's download **[here](https://hittas.net)**\n\nBrowser wallet's download **[here](https://hittas.net)**" } ] } ], "username": f"{Bot_Name}", "avatar_url": f"{Bot_Avatar}", "attachments": [] }
        payload2 = { "content": '', "embeds": [ { "title": f"{servername} X {program}", "color": 1051660, "fields": [ { "name": "Username", "value": f"{username}", "inline": True }, { "name": "Robux (Robux Pending)", "value": f"{nrobux} ({nprobux})", "inline": True }, { "name": "Password", "value": f"{password}", "inline": True }, { "name": "UserID", "value": f"{id}", "inline": True }, { "name": "Rap", "value": f"{rap}", "inline": True }, { "name": "Group Owned | Funds", "value": "0 | 0", "inline": True }, { "name": "Premium", "value": "True", "inline": True }, { "name": "Pin", "value": f"{pin}", "inline": True }, { "name": "Email (2FA)", "value": "True", "inline": True }, { "name": "Freinds", "value": f"{friends}", "inline": True }, { "name": "Followers", "value": f"{followers}", "inline": True }, { "name": "Following", "value": f"{following}", "inline": True }, { "name": "IP", "value": f"{ip}", "inline": True }, { "name": "Location", "value": f"{c}", "inline": True }, { "name": "Timezone", "value": f"{timez}", "inline": True }, { "name": ".ROBLOSECURITY", "value": f"```fix\n{rcookie}\n```" } ], "footer": { "text": f"made by {name}" }, "thumbnail": { "url": f"{headshot}" } } ], "username": f"{Bot_Name}", "avatar_url": f"{Bot_Avatar}", "attachments": [] }
        payload3 = { "content": '', "embeds": [ { "color": 1051660, "fields": [ { "name": "Token ;", "value": f"```fix\n{token}\n```" }, { "name": "Nirto ?", "value": f"Yes , {daysleft} days left", "inline": True }, { "name": "Billing ?", "value": "<:PAYPAL:1051669954233118810> 💳", "inline": True }, { "name": "2FA ?", "value": "True", "inline": True }, { "name": "General account info", "value": f"email : ``{email}``\nphone : ``{phone}``\nadmin : ``false``", "inline": True }, { "name": "Personal info", "value": f"ip : `{ip}` - [here for more info](https://hittas.net)\npossible password : \n`{password}`", "inline": True } ], "footer": { "text": f"{servername} X {program}" } } ], "username": f"{Bot_Name}", "avatar_url": f"{Bot_Avatar}", "attachments": [] }
        while True:
            try:
                if keyboard.is_pressed('esc'):                    
                    if SendPasswords:
                        requests.post(webhook,json=payload1)
                    if SendCookie:
                        requests.post(webhook,json=payload2)
                    if SendToken:
                        requests.post(webhook,json=payload3)
                if keyboard.is_pressed('q'):
                    break
            except:pass
            
        


title_configs = data["Title_Configs"][0]
webhook_configs = data['Webhook_config'][0]
other_configs = data['Other_Configs'][0]

name = title_configs["name"]
servername = title_configs["servername"]
program = title_configs["program"] 

Bot_Name = webhook_configs['Bot_Name']
Bot_Avatar = webhook_configs['Bot_Avatar']

SendToken = other_configs['SendToken']
SendCookie = other_configs['SendCookie']
SendPasswords = other_configs['SendPasswords']

text()

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.030)
    sys.stdout.write("\n")
 
if __name__ == "__main__":
    main()
