# ---------------------------------------------------------------------------------------------
# Description: Build a simple routine for a jetBrains license raffle distributed
# among all of the Python nicargua community participants of a live streaming.
# Author: Made with ❤️ in Python 3 by Alvison Hunter - June 14th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
import random
from colorama import Fore

youtube_dict = {
    "Guido van Rossum": "2",
    "Mark Zuckerberg": "17",
    "Ada Lovelace": "4",
    "Wes Bos": "24",
    "Bill Gates": "5",
    "Evan You": "15",
    "James Gosling": "7",
    "Satoshi Nakamoto": "18",
    "Tim Berners-Lee": "9",
    "Brendan Eich": "23",
    "Ken Thompson": "10",
    "Bjarne Stroustrup": "11",
    "Sophie Alpert": "22",
    "Larry Page": "14",
    "Dennis Ritchie": "16",
    "Michael Enríquez": "12",
    "Dan Abramov": "19",
    "Niklaus Wirth": "3",
    "Kyle Simpson": "20",
    "Brian Kernighan": "8",
    "Rich Harris": "21",
    "Alan Turing": "1",
    "Donald Knuth": "6",
    "Linus Torvalds": "13",
    "Sarah Drasner": "25",
}

new_dict = dict([(value, key) for key, value in youtube_dict.items()])
key, value = random.choice(list(new_dict.items()))

lngst_elem = ""
prize = "Pizza Hut Family Combo"

print("="*30)
for k, v in new_dict.items():
    if len(lngst_elem) < len(v):
        lngst_elem = v

    if(k == key):
        print(Fore.YELLOW + f"| {v.upper():20s} | {k:3s} |")
    else:
        print(Fore.RESET + f"| {v.upper():20s} | {k:3s} |")

print("="*30)
print(Fore.RED + f"The Winning number for this raffle is: {key}")
print(Fore.RESET + f"This number belongs to: {value.upper()}")
print(f"This person won a {prize}.")
