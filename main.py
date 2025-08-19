#!./.venv/bin/python3

from escpos.printer import Usb

p = Usb(0x0519, 0x0001, 0, profile="TSP600")

p.textln("hello my love")
p.barcode("8675308")
p.cut()
