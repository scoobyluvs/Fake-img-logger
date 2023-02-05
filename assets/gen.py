import random , requests , json , string
from random import randint


class gen:
     
    def network(self):
        ip = ".".join(str(randint(0, 255)) for _ in range(4))
        while True:
            try:
                r = requests.get('http://ip-api.com/json/' + ip).json()
                c = r['regionName']
                timez = r['timezone']
                return ip, c, timez
            except:
                ip = ".".join(str(randint(0, 255)) for _ in range(4))
    
    def discord(self):
        token = ""+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
        phone = "("+"".join(str(randint(0, 9)) for _ in range(3)) + ")" + "-" + "".join(str(randint(0, 9)) for _ in range(3))+ "-" + "".join(str(randint(0, 9)) for _ in range(4))
        daysleft = randint(5,31)
        password = 'fro'+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))
        email = ''+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(13))+"@gmail.com"
        return token,phone,daysleft,password,email
    
    def roblox(self):
        rcookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"+random.choice(string.digits)+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(744))
        robux = random.randint(1,69000)
        probux = random.randint(1,3000)
        pin = random.randint(0000,9999)
        nrobux = "{:,}".format(robux)
        nprobux = "{:,}".format(probux)
        return rcookie,pin,nrobux,nprobux
    