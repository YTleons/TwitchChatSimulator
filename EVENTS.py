import NICKNAMES
from random import randint

vals = ["рублей", "тенге", "долларов", "евро"]

a = [
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} задонатил {randint(100, 10000)} {vals[randint(0, len(vals) - 1)]} !",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} подарил {randint(5, 1000)} сабок!",
    f"{NICKNAMES.a[randint(0, len(NICKNAMES.a) - 1)]} рейдит канал с {randint(5, 10000)} подписчиками!"
]