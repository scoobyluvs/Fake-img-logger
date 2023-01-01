COLORS = { "black":"\u001b[30;1m", "red": "\u001b[31;1m", "green":"\u001b[32m", "yellow":"\u001b[33;1m", "blue":"\u001b[34;1m", "magenta":"\u001b[35m", "cyan": "\u001b[36m", "white":"\u001b[37m", "yellow-background":"\u001b[43m", "black-background":"\u001b[40m", "cyan-background":"\u001b[46;1m", }

class text():


    def __init__(self) -> None:
        self.colors()

    def colorText(self,text):
        for color in COLORS:
            text = text.replace("[[" + color + "]]", COLORS[color])
        return text
    
    def colors(self):
        f  = open("assets/text.txt","r",encoding="utf8")
        ascii = "".join(f.readlines())
        print(self.colorText(ascii))