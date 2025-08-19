# Ticket Gremlin (gremlin)

> Author: [Kyle Beasley](www.github.com/krbeasely)

A small python program that prints "Work Tickets", notes, tasks, etc on a Star Micronics TSP650. I mean the OG version released sometime between 1995 and 2005. Not the TSP650ii. However the program should still work. This is also only tested on Linux (Debian 13). Other operating systems (and other flavors of linux) might find this program unusable.

> Inspired by CodingWithLewis's YouTube Video, *I Fixed My ADHD with a Receipt Printer*. I watched the first 23 seconds, said "That's genius I need to do this" and clicked off to Ebay. Thank you for the inspiration Lewis! I've since gone back and finished the video. <3
>
> [Full Vid Here](https://www.youtube.com/watch?v=xg45b8UXoZI)

---

### Coming Features:

- Auto-Configuration: The first time gremlin runs, it will ask you to create a configuration file to store some basic information like your printer type (for when more printers are supported) and (possibly) users that will be sending tickets. 

---

## Installation

1. Clone the repo wherever you keep your applications.

```$ git clone git@github.com:krbeasley/TicketGremlin && cd TicketGremlin```

2. Create a Virtual Environment for gremlin to live in. (You don't want him escaping)

```python3 -m venv .venv```

3. Install the dependencies.

> Wait! You should inspect the requirements.txt file and ensure it fits your needs. Notice that only the "Usb" portion of the escpos package is used. My printer is connected via USB, therefore that's all gremlin supports. Serial, Network, and Bluetooth functionality will have to wait until I can get my hands on a thermal printer released within the last 2 decades.

```$ pip install -r requirements.txt```

4. \[Optional\] Create an alias for gremlin.
    - Make gremlin's `main.py` file executable. ```chmod u+x main.py```
    - Using your editor of choice, modify your ```~/.bash_aliases``` file.
    - On a new line, enter the following:
    ```alias gremlin="/home/your/install/dir/TicketGremlin/main.py"```
    - Run ```source ~/.bashrc``` and ```gremlin``` becomes a globally available resource.

5. \[Not Optional\] Ensure you have permission to use the printer.

    - Enter ```cat /etc/group | grep $USER``` into your terminal to view all of the groups you are a part of.
    - If you do not see your username included in the "lp" group, add yourself (assuming you have sudo permission) by entering ```sudo usermod -aG lp <your_username>```. The next time you log into your shell, you will have the necessary permissions.

6. Give it a shot! Run ```gremlin --print-config``` to see what happens.

## Basic Usage

Printing tasks is extremely simple. Simply provide gremlin with a `-m` message and he'll print it for you. Optionally, you can include a `-t` title.

```
gremlin -t "This is my task!"\
-m "There are many more like it but this one is mine!"
```

Prints the ticket:

```

2025-08-19 -- 13:10:30
This is my task!

There are many more like it but this one 
is mine!

```

To pass a due date onto a task, specify it with the ```-d``` flag. Any date can be passed as long as it's in the ```MMDDYYYY``` format. (I'm American, okay?). You may also pass along ```ASAP``` to emphasize the urgency of this task.

```
gremlin -m "I have to have this done soon." -d "04202025"
```

Prints:

```

2025-08-19 -- 13:10:30

Due: 04/20/2025

I have to have this done soon.

```

## Troubleshooting

### "My printer kinda-sorta prints right? And the cut function isn't working..."

> Your Star Micronics TSP650 does not fully understand the ESC/POS commands this application uses. To put your printer in ESCPOS mode, you must flip `Dip Switch 1-1` from `On` to `Off`. Turn off your printer first. Unplug it even.

1. Flip your printer.
2. Using a Philips head screwdriver, unscrew the Dip Switch cover plate from the base of the printer.
3. Locate the wider of the two Dip Switch sets. Find the switch labeled "1" (furthest left) and flip it off.
4. Reassemble your printer and turn it back on.
5. Try to run it again.

---

## Todo

- Allow for line breaks in messages.
