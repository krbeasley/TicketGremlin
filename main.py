#!./.venv/bin/python3

from escpos.printer import Usb
p = Usb(0x0519, 0x0001, 0, profile="TSP600")

p.text("this is a test")
p.ln(20)
p.cut()
