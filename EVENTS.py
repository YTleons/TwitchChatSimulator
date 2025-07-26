import NICKNAMES
from random import randint

vals = ["рублей", "тенге", "долларов", "евро"]
streamername = None
banreasons = ["пишет плохие слова", "скинул 18+ в чат", "курит", "ест наркотики", "чиловый парень", "пдф"]
a = [
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} задонатил {randint(100, 10000)} {vals[randint(0, len(vals) - 1)]} !",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} подарил {randint(5, 1000)} сабок!",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} рейдит канал с {randint(5, 10000)} подписчиками!",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} покупает подписку буси на {randint(3, 10)} месяца!",
    f"{streamername} забанил {NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} по причине: {banreasons[randint(0, len(banreasons))]}"
]

def reload_list():
    a = [
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} задонатил {randint(100, 10000)} {vals[randint(0, len(vals) - 1)]} !",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} подарил {randint(5, 1000)} сабок!",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} рейдит канал с {randint(5, 10000)} подписчиками!",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} покупает подписку буси на {randint(3, 10)} месяца!",
    f"{streamername} забанил {NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} по причине: {banreasons[randint(0, len(banreasons))]}"
]