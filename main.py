#!./.venv/bin/python3

import argparse
from Printers.StarPrinter import StarPrinter
from Printables.Message import Message
from Printables.Task import Task

GremlinConfig = {
    "name": "Gremlin",
    "version": "0.1.0"
}

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
                          "dates should be in the format MMDDYYYY or ASAP "))
parser.add_argument("--feed-cut", action='store_true',
                    help="Feed and cut the paper, ignoring other commands.")
parser.add_argument("--print-config", action='store_true',
                    help="Print the current gremin configuration settings.")


def die(message, code=1):
    print(f"Error: {message}")
    exit(code)


# Load the printer
printer = StarPrinter()

if __name__ == "__main__":
    args = parser.parse_args()
    printer.device.open()  # Open the printer connection.

    if args.feed_cut is True:
        # Check if the user is just asking to feed and cut
        printer.device.ln()  # Feed the roll by one line
        printer.cut()
    else:
        # Check if we should print the config
        if args.print_config is True:
            printer.printNow()
            printer.writeLine(f"Name: {GremlinConfig['name']}")
            printer.writeLine(f"Verson: {GremlinConfig['version']}")
        else:
            # Print the task / message / thingy
            if args.m is None:
                die("You must provide a message")

            message = Message(body=args.m)

            if args.d is not None:
                message = Task(body=args.m, due_date=args.d)

            if args.t is not None:
                message.setSubject(args.t)
        # Print the message / task
        printer.printMessage(message)

        # Cut the roll
        printer.cut()

    # We close printer connections around here
    printer.device.close()
