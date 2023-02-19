import os
import sys
import time
import requests
import keyboard
from colorama import Fore
from assets.checker import Roblox
from assets.gen import gen
from assets.banner import Text
from assets.config import Config

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

config = Config('config.json')
gen = gen()

class Main:
    def __init__(self) -> None:
        self.userinput()

    def print015(self, text):
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

    def build(self, image: str) -> None:
        with open("build/logger.png", 'wb') as f:
            r = requests.get(image, stream=True, verify=False)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)

    def post(self, webhook: str) -> None:
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Enter the roblox id you want to beam')
        id = input('> ')
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Checking roblox api...')
        username, headshot, rap, friends, followers, following = Roblox.check_user(id)
        ip, c, timez = gen.network()
        token, phone, daysleft, password, email = gen.discord()
        rcookie, pin, nrobux, nprobux = gen.roblox()
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Enter the discord img url')
        image = input("> ")
        self.build(image)
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Building image...')
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Checking for VS...')
        time.sleep(3)
        self.print015(f'{Fore.RED}[{config.program}]{Fore.WHITE} Built ! check build folder')

        payload1 = {
            "content": "@everyone",
            "embeds": [{
                "title": "Someone just ran your image !",
                "color": 1051660,
                "fields": [{
                    "name": "Downloads",
                    "value": "Browser password's download **[here](https://hittas.net)**\n\nBrowser cookie's download **[here](https://hittas.net)**\n\nBrowser history's download **[here](https://hittas.net)**\n\nBrowser wallet's download **[here](https://hittas.net)**"
                }]
            }],
            "username": f"{config.bot_name}",
            "avatar_url": f"{config.bot_avatar}",
            "attachments": []
        }
        payload2 = {
            "content": '',
            "embeds": [{
                "title": f"{config.servername} X {config.program}",
                "color": 1051660,
                "fields": [{
                    "name":
