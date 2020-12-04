# Made with ❤️ in Python 3 by Alvison Hunter - November 30th, 2020
def fill_chars(initfill,endfill, rows):
    n = int(rows)
    lst_results = []
    for fc in range(1,rows+1):
        rightfiller = endfill*fc
        leftfiller = initfill*n
        lst_results.append(leftfiller+rightfiller)
        n -=1
    for item in lst_results:
        print(' '.join(item))
#let's pass the params to the function o'er here now
fill_chars('#','@',6)
#Greetings from Jinotepe, Nicaragua!



