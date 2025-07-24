import NICKNAMES
import SUFFIXES
import PREFIXES
import MESSAGES
import EVENTS
import YEAR
from colorama import init, Fore
from random import randint, randrange
from time import sleep
init(autoreset=True)

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.YELLOW]

print("Twitch chat simulator pre-release by Yar_developer")
streamername = input("Введите имя стримера: ")
MESSAGES.streamername = streamername
print(Fore.GREEN + f"{streamername} начал свой стрим!")

while True:
    MESSAGES.streamername = streamername
    MESSAGES.reload_list()
    if randint(0, 100) == 50:
        print(Fore.GREEN + "======================================================")
        print()
        print()
        print()
        print(Fore.RED + EVENTS.a[randint(0, len(EVENTS.a) - 1)])
        print()
        print()
        print()
        print(Fore.GREEN + "======================================================")
    else:
        sleep(randint(900, 3000) / 1000)
        YEAR.a = randint(2000, 2021)
        print(colors[randint(0, 5)] + NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)] + PREFIXES.a[randint(0, len(PREFIXES.a) - 1)] + ": " + MESSAGES.a[randint(0, len(MESSAGES.a) - 1)])