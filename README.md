# Ticket Gremlin (gremlin)

> Author: [Kyle Beasley](www.github.com/krbeasely)

A small python program that prints "Work Tickets", notes, tasks, etc on a Star Micronics TS650. I mean the OG version released sometime between 1995 and 2005. Not the TS650ii. However the program should still work. This is also only tested on Linux (Debian 13). Other operating systems (and other flavors of linux) might find this program unusable.

> Inspired by CodingWithLewis's YouTube Video, *I Fixed My ADHD with a Receipt Printer*. I watched the first 23 seconds, said "That's genius I need to do this" and clicked off to Ebay. Thank you for the inspiration Lewis! I've since gone back and finished the video. <3
>
> [Full Vid Here](https://www.youtube.com/watch?v=xg45b8UXoZI)

---

### Coming Features:

- Auto-Configuration: The first time gremlin runs, it will ask you to create a configuration file to store some basic information like your printer type (for when more printers are supported) and (possibly) users that will be sending tickets. 

- Task Due Dates: This is pretty self-explanatory and definitely something every ticketing system needs. Rest-assured it's coming.

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
    - Using your editor of choice, modify your ```~/.bash_aliases``` file.
    - On a new line, enter the following:
    ```alias gremlin="python3 /your/install/dir/TicketGremlin/main.py"```
    - Run ```source ~/.bashrc``` and ```gremlin``` becomes a globally available resource.

5. \[Not Optional\] Ensure you have permission to use the printer.

    - Enter ```cat /etc/group | grep $USER``` into your terminal to view all of the groups you are a part of.
    - If you do not see your username included in the "lp" group, add yourself (assuming you have sudo permission) by entering ```sudo usermod -aG lp <your_username>```. The next time you log into your shell, you will have the necessary permissions.

6. Give it a shot! Run ```gremlin --print-config``` to see what happens.

## Basic Usage

```gremlin -t "This is my task!" -m "There are many more like it but this one is mine!"```

Prints the ticket:

```

2025-08-19 -- 13:10:30
This is my task!

There are many more like it but this one 
is mine!

```

## Troubleshooting

