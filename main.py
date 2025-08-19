#!./.venv/bin/python3

from escpos.printer import Usb

p = Usb(0x0519, 0x0001, 0, profile="TSP600")

p.textln("this is some text")
p.barcode("8675309", "CODE39", width=3)
p.qr(123456789)
p.cut()
