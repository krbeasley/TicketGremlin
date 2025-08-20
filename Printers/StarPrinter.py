from escpos.printer import Usb
from datetime import datetime
from Printables import Message

MAX_LINE_LEN = 42


class StarPrinter:
    def __init__(self):
        self.device = Usb(0x0519, 0x0001, 0, profile="TSP600")
        self.max_line_len = 42

    def printMessage(self, message):
        self.printNow()
        for line in message.render():
            self.writeLine(line)

    def writeLine(self, line):
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

    def printDueDate(self, dueDate):
        if str(dueDate).upper() != "ASAP":
            now = datetime.strptime(dueDate, "%m%d%Y")
            self.writeLine("Due: " + now.strftime("%m/%d/%Y"))
        else:
            self.writeLine("Due: ASAP")
            self.device.ln()
