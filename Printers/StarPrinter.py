from escpos.printer import Usb
from datetime import datetime

MAX_LINE_LEN = 42


def getNChars(text, n):
    """Returns the first n characters from a line of text"""
    return text[:n]


def makeTextList(text):
    """Create a list of text lines short enough to fit on a roll"""
    text_list = []

    """Loop through the text until the length is less than the
        maximum amount"""
    while (len(text) > MAX_LINE_LEN):
        i = 0  # Number of loops for this
        nChar = getNChars(text, MAX_LINE_LEN)
        while nChar[-1] != " ":
            if i > 100:
                print("ERROR: Looped too much when making a test list")
                exit(1)

            nChar = getNChars(text, MAX_LINE_LEN - i)
            i = i + 1

        text_list.append(nChar)
        text = str(text).replace(nChar, "")

    # Push the remaining text to the buffer
    text_list.append(text)
    return text_list


class StarPrinter:
    def __init__(self):
        self.device = Usb(0x0519, 0x0001, 0, profile="TSP600")
        self.max_line_len = 42

    def writeLine(self, text):
        text_list = makeTextList(text)
        for line in text_list:
            self.device.textln(line)

    def writeBarcode(self, data, format="CODE39"):
        self.device.barcode(data, format, width=3)

    def writeQR(self, data):
        self.device.qr(data, size=5)

    def cut(self):
        self.device.cut()

    def printNow(self):
        now = datetime.today().strftime("%H:%M:%S -- %m/%d/%Y")
        self.writeLine(now)
