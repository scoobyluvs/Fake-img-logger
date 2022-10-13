import json, requests,random,string,time
from random import randint

# - stuff to fill out
webhook = ''
name = ''
madeby = ''
delay = 0

# - true or false
SendCookie = True
SendToken = True

def stuff():
	ip = ".".join(str(randint(0, 255)) for _ in range(4))
	daysleft = randint(5,31)
	token = ""+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
	phone = "("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))
	tokenid = random.randint(100000000000000000, 999999999999999999)
	rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.ascii_uppercase)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
	robux = random.randint(1,69000)
	probux = random.randint(1,3000)
	rap = random.randint(10000,250000)
	return ip,daysleft,token,phone,tokenid,rcookie,robux,probux,rap
def cookie():
	ip,daysleft,token,phone,tokenid,rcookie,robux,probux,rap = stuff()
	nrap = "{:,}".format(rap);nrobux = "{:,}".format(robux);nprobux = "{:,}".format(probux)
	info = {
    "content": '',
    "embeds": [
      {
        "title": f":rocket:  - NEW HIT , .gg/comped X {madeby}",
        "color": 15654879,
        "fields": [
          {
            "name": "Robux (pending)",
            "value": f"{nrobux} ({nprobux})",
            "inline": True
          },
          {
            "name": "Premium",
            "value": "True",
            "inline": True
          },
          {
            "name": "RAP",
            "value": f"{nrap}",
            "inline": True
          },
          {
            "name": ".ROBLOSECURITY",
            "value": f"```fix\n{rcookie}```"
          }
          ]
      }
    ],
    "username": f"{name} - .gg/comped X {madeby}",
    "attachments": []
    }
	requests.post(webhook, json=info)
def tokensend():
	ip,daysleft,token,phone,tokenid,rcookie,robux,probux,rap = stuff()
	info = {
  "content": '',
  "embeds": [
    {
      "title": f":rocket:  - TOKEN GRABBED , .gg/comped X {madeby}",
      "color": 15654879,
      "fields": [
        {
          "name": "__Account Information__",
          "value": f"Phone: `{phone}`\n2FA/MFA Enabled: `True`\nNitro: `True`\nExpires in: `{daysleft}`\nID : `{tokenid}`",
          "inline": True
        },
        {
          "name": "__TOKEN__",
          "value": f"`{token}`"
        }
      ],
      "footer": {
        "text": f".gg/comped X {madeby}"
      }
    }
  ],
  "username": f"{name} - .gg/comped X {madeby}",
  "avatar_url": "https://media.discordapp.net/attachments/964167979438841906/1027571131076591626/unknown.png",
  "attachments": []
	}
	requests.post(webhook, json=info)
def post():
	time.sleep(delay)
	sendem = {
  	"content": '',
  	"embeds": [
    {
      "color": 15064798,
      "footer": {
        "text": ".gg/comped | scooby#0001"
      },
      "image": {
        "url": "https://media.discordapp.net/attachments/818904708940693513/1028385554242486333/unknown.png?width=675&height=675"
      }
    }
  ],
  "username": "scooby's sex slave",
  "attachments": []
	}
	requests.post(webhook, json=sendem)
	if SendCookie and SendToken:
		tokensend()
		cookie()
		exit()
	if SendCookie:
		cookie()
		exit()
	if SendToken:
		tokensend()
		exit()

if __name__ == '__main__':
	post()
