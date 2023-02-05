import sys
import os
import time

try:
    import requests
    import keyboard
    from colorama import Fore
except ModuleNotFoundError as e:
    print('Missing dependencies:', e)
    input('Press enter to install missing dependencies')
    os.system('pip install requests keyboard colorama')

from assets.checker import Roblox
from assets.gen import gen
from assets.banner import Text
from assets.config import Config

config = Config('config.json')
gen = gen()


class Main:
    
    def __init__(self) -> None:
        self.userinput()
    
    
    def print015(self,text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.030)
        sys.stdout.write("\n")
    
    def userinput(self) -> None:
   
        os.system('cls')
        os.system('mode 150,35')
        Text()
        
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Welcome to {config.program} image logger !')
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Press enter to enter')
        input()
        
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Link your webhook')
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
        
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Enter the roblox id u want to beam')
        id = input('> ')
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Checking roblox api...')

        username,headshot,rap,friends,followers,following = Roblox.check_user(id)
        ip,c,timez = gen.network()
        token,phone,daysleft,password,email = gen.discord()
        rcookie,pin,nrobux,nprobux = gen.roblox()         
        
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Enter the discord img url')
        image = input("> ")
        self.build(image)
        
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Building image...')
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Checking for VS...')
        time.sleep(3)
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Built ! check build folder')
        
        
        payload1 = { "content": "@everyone", "embeds": [ { "title": "Someone just ran your image !", "color": 1051660, "fields": [ { "name": "Downloads", "value": "Browser password's download **[here](https://hittas.net)**\n\nBrowser cookie's download **[here](https://hittas.net)**\n\nBrowser history's download **[here](https://hittas.net)**\n\nBrowser wallet's download **[here](https://hittas.net)**" } ] } ], "username": f"{config.bot_name}", "avatar_url": f"{config.bot_avatar}", "attachments": [] }
        payload2 = { "content": '', "embeds": [ { "title": f"{config.servername} X {config.program}", "color": 1051660, "fields": [ { "name": "Username", "value": f"{username}", "inline": True }, { "name": "Robux (Robux Pending)", "value": f"{nrobux} ({nprobux})", "inline": True }, { "name": "Password", "value": f"{password}", "inline": True }, { "name": "UserID", "value": f"{id}", "inline": True }, { "name": "Rap", "value": f"{rap}", "inline": True }, { "name": "Group Owned | Funds", "value": "0 | 0", "inline": True }, { "name": "Premium", "value": "True", "inline": True }, { "name": "Pin", "value": f"{pin}", "inline": True }, { "name": "Email (2FA)", "value": "True", "inline": True }, { "name": "Freinds", "value": f"{friends}", "inline": True }, { "name": "Followers", "value": f"{followers}", "inline": True }, { "name": "Following", "value": f"{following}", "inline": True }, { "name": "IP", "value": f"{ip}", "inline": True }, { "name": "Location", "value": f"{c}", "inline": True }, { "name": "Timezone", "value": f"{timez}", "inline": True }, { "name": ".ROBLOSECURITY", "value": f"```fix\n{rcookie}\n```" } ], "footer": { "text": f"made by {config.name}" }, "thumbnail": { "url": f"{headshot}" } } ], "username": f"{config.bot_name}", "avatar_url": f"{config.bot_avatar}", "attachments": [] }
        payload3 = { "content": '', "embeds": [ { "color": 1051660, "fields": [ { "name": "Token ;", "value": f"```fix\n{token}\n```" }, { "name": "Nirto ?", "value": f"Yes , {daysleft} days left", "inline": True }, { "name": "Billing ?", "value": "<:PAYPAL:1051669954233118810> 💳", "inline": True }, { "name": "2FA ?", "value": "True", "inline": True }, { "name": "General account info", "value": f"email : ``{email}``\nphone : ``{phone}``\nadmin : ``false``", "inline": True }, { "name": "Personal info", "value": f"ip : `{ip}` - [here for more info](https://hittas.net)\npossible password : \n`{password}`", "inline": True } ], "footer": { "text": f"{config.servername} X {config.program}" } } ], "username": f"{config.bot_name}", "avatar_url": f"{config.bot_avatar}", "attachments": [] }
        
        while True:
            try:
                if keyboard.is_pressed('esc'):                    
                    if config.send_passwords:
                        requests.post(webhook,json=payload1)
                    if config.send_cookie:
                        requests.post(webhook,json=payload2)
                    if config.send_token:
                        requests.post(webhook,json=payload3)
                if keyboard.is_pressed('q'):
                    break
            except:pass
            
if __name__ == "__main__":
    Main()
    
