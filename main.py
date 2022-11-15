import requests
import sys
import time
import robloxpy
import json
import random
import string
import os
from random import randint
from colorama import Fore

os.system('cls')

COLORS = {
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}
def colorText(text):
  for color in COLORS:
    text = text.replace("[[" + color + "]]", COLORS[color])
  return text
f  = open("Main/text.txt","r",encoding="utf8")
ascii = "".join(f.readlines())
print(colorText(ascii))





class main():
  def __init__(self):
    self.userinput()
  
  def print015(self,text):
    for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.030)
    sys.stdout.write("\n")
  
  def userinput(self):
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} A Python Fake Img logger')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} .gg/comped ')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} made by scooby ')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} hittas.net ')
    time.sleep(3)
    os.system('cls')
    print(colorText(ascii))
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} Please enter your webhook below')
    webhook = input('---> ')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} Please input the roblox ID')
    rid = input('---> ')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} Please input the Name')
    name = input('---> ')
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} Please input whose it made by')
    madeby = input('---> ')
    self.post(webhook,rid,name,madeby)
  
  def getinfo(self):
    ip = ".".join(str(randint(0, 255)) for _ in range(4))
    r = requests.get('http://ip-api.com/json/' + ip).json()
    c = r['regionName']
    timez = r['timezone'] 
    rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.ascii_uppercase)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
    password = 'fro'+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))
    daysleft = randint(5,31)
    tokenid = random.randint(100000000000000000, 999999999999999999)
    token = ""+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
    phone = "("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))
    # dont change usally 
    
    robux = random.randint(1,69000) # // only uncomment if u want it to be a certian number // robux = numberhere
    probux = random.randint(1,3000) # // only uncomment if u want it to be a certian number // probux = numberhere
    pin = random.randint(0000,9999) # // only uncomment if u want it to be a certian number // pin = pinhere
    
    return ip,timez,c,rcookie,robux,probux,pin,password,daysleft,tokenid,token,phone
  
  def post(self,webhook,rid,name,madeby):
    ip,timez,c,rcookie,robux,probux,pin,password,daysleft,tokenid,token,phone = self.getinfo()
    nrobux = "{:,}".format(robux)
    nprobux = "{:,}".format(probux)
    username = robloxpy.User.External.GetUserName(rid)
    headshot = robloxpy.User.External.GetHeadshot(rid)
    nrap = robloxpy.User.External.GetRAP(rid)
    rap = "{:,}".format(nrap)
    friends = robloxpy.User.Friends.External.GetCount(rid)
    followers = robloxpy.User.Friends.External.GetFollowerCount(rid)
    following = robloxpy.User.Friends.External.GetFollowingCount(rid)
    tinfo = {"content": '',"embeds": [{"title": f":rocket: - TOKEN GRABBED , .gg/comped X {madeby}","color": 15654879,"fields": [{"name": "__Account Information__","value": f"Phone: `{phone}`\n2FA/MFA Enabled: `True`\nNitro: `True`\nExpires in: `{daysleft}`\nID : `{tokenid}`","inline": True},{"name": "__TOKEN__","value": f"`{token}`"}],"footer": {"text": f".gg/comped X {madeby}"}}],"username": f"{name} - .gg/comped X {madeby}","avatar_url": "https://media.discordapp.net/attachments/964167979438841906/1027571131076591626/unknown.png","attachments": []}
    info = {"content":'',"embeds":[{"title":":rocket: - NEW HIT , S3X x .gg/comped","color":16077394,"fields":[{"name":"Username","value":f"{username}","inline":True},{"name":"Robux (Robux Pending)","value":f"{nrobux} ({nprobux})","inline":True},{"name":"Password","value":f"{password}","inline":True},{"name":"UserID","value":f"{rid}","inline":True},{"name":"Rap","value":f"{rap}","inline":True},{"name":"Group Owned | Funds","value":"0 | 0","inline":True},{"name":"Premium","value":"True","inline":True},{"name":"Pin","value":f"{pin}","inline":True},{"name":"Email (2FA)","value":"True","inline":True},{"name":"Freinds","value":f"{friends}","inline":True},{"name":"Followers","value":f"{followers}","inline":True},{"name":"Following","value":f"{following}","inline":True},{"name":"IP","value":f"{ip}","inline":True},{"name":"Location","value":f"{c}","inline":True},{"name":"Timezone","value":f"{timez}","inline":True},{"name":".ROBLOSECURITY","value":f"```fix\n{rcookie}\n```"}],"footer":{"text":".gg/comped"},"thumbnail":{"url":f"{headshot}"}}],"username":".gg/comped X s3x","avatar_url":"https://media.discordapp.net/attachments/818894451018956801/1014985705023361177/52D8396A-A6FB-4BE9-966D-1E2891B56586.gif","attachments":[]}
    #time.sleep(0)
    requests.post(webhook, json=info)
    requests.post(webhook,json=tinfo)
    self.print015(f'{Fore.RED}[.gg/comped]{Fore.WHITE} Sent to your webhook')
    input('\nenter to exit.')


if __name__ == "__main__":
  main()

