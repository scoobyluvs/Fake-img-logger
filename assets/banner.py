class Text:
    
    COLORS = {
        "black": "\u001b[30;1m",
        "red": "\u001b[31;1m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33;1m",
        "blue": "\u001b[34;1m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m"
    }

    def __init__(self):
        self.colors()

    def color_text(self, text):
        for color in self.COLORS:
            text = text.replace("[[" + color + "]]", self.COLORS[color])
        return text

    def colors(self):
        with open("assets/text.txt", "r", encoding="utf8") as f:
            ascii_text = "".join(f.readlines())
        print(self.color_text(ascii_text))