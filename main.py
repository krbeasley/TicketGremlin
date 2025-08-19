#!./.venv/bin/python3

import argparse
from StarPrinter import StarPrinter
from datetime import datetime


parser = argparse.ArgumentParser(
    description=("Simple python script to print tickets and reminders on a "
                 "Star Micronics TSP650"),
    epilog="View the source @ github.com/krbeasley/TicketPrinter"
)
parser.add_argument("-t", default=None, metavar="title",
                    help="[Optional] The title of the ticket")
parser.add_argument("-m", default=None, metavar="message",
                    help="The message for the ticket")
parser.add_argument("-d", default=None, metavar="due",
                    help=("[Optional] The due date of the ticket. Supplied "
                          "dates should be in the format MMDDYYYY or ASAP"))
parser.add_argument("--feed-cut", action='store_true',
                    help="Feed and cut the paper, ignoring other commands.")


def die(message, code=1):
    print(f"Error: {message}")
    exit(code)


# Load the printer
printer = StarPrinter()

if __name__ == "__main__":
    args = parser.parse_args()

    printer.device.open()

    if args.feed_cut is True:
        printer.device.ln()  # Feed the roll by one line
        printer.cut()
    else:
        if args.m is None:
            die("You must provide a message")

        # Print the date for the ticket
        now = datetime.today().strftime("%H:%M:%S -- %m/%d/%Y")
        printer.writeLine(now)

        if args.t is not None:
            # Print the title to the ticket
            printer.writeLine(args.t)
            printer.device.ln()  # Extra padding on the bottom of the title

        printer.device.ln()
        printer.writeLine(args.m)
        printer.cut()

    printer.device.close()
