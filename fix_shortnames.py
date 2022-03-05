#----------------------------------------------------------------------------
# Your organisation uses lowercase shortnames with 2 first letters of first
# and last name. Go through team dictionary and fix the shortnames.
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - January 22nd, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
#----------------------------------------------------------------------------


team = {
    "John Cleese": "jocl",
    "Eric idle": "ecil",
    "michael palin": "mipa",
    "graham Chapman": "grry",
    "Terry Gilliam": "teg",
    "terry jones": "TEJO",
}

print({i:str(i[:2]+i[i.find(" ")+1:i.find(" ")+3]).lower() for i in team.keys()})

[print(i) for i in range(1,22) if (i%2==0)]