# ROT13 is a simple letter substitution cipher that replaces a letter with

# Made with ❤️ in Python 3 by Alvison Hunter - April 7th, 2021
equivalency = {"А": "a",
               "Б": "b",
               "В": "v",
               "Г": "g",
               "Д": "d",
               "Е": "e",
               "Ё": "io",
               "Ж": "zh",
               "З": "z",
               "И": "i",
               "Й": "y",
               "К": "k",
               "Л": "l",
               "М": "m",
               "Н": "n",
               "О": "o",
               "П": "p",
               "Р": "r",
               "С": "s",
               "Т": "t",
               "У": "u",
               "Ф": "f",
               "Х": "x",
               "Ц": "ts",
               "Ч": "ch",
               "Ш": "sh",
               "Щ": "shch",
               "Ъ": "ъ",
               "Ы": "i",
               "Ь": "ь",
               "Э": "e",
               "Ю": "yu",
               "Я": "ya"
               }


def russian_to_english(message):
    str_translation = ""
    message = message.upper()
    print(f"Transforming to upper: {message}")
    msg_lst = message.split()
    for letter in msg_lst:
        str_translation += ''.join([str(equivalency[el].upper())
                                   for el in letter]) + " "

    print(f"Transcoded Phrase: {str_translation}")


# let us call the function with capitalized text
russian_to_english("Дуарте Евангелиста Джон Иван")
