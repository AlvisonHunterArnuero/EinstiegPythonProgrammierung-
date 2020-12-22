import numpy as np
def is_solved(board):
    board = np.array(board)
    eins = False
    zwei = False

    for el in range(0,3):
        zeile = board[el,:]
        print(zeile)
        resultat = summe_prufen(zeile)
        if resultat == 1:
            eins = True
        elif resultat == 2:
            zwei = True

    for el in range(0,3):
        spalte = board[:,el]
        resultat = summe_prufen(spalte)
        if resultat == 1:
            eins = True
        elif resultat == 2:
            zwei == True

    diagonal1 = np.diagonal(board)
    resultat = summe_prufen(diagonal1)
    if resultat == 1:
        eins = True
    elif resultat == 2:
        zwei == True

    diagonal2 = np.rot90(board).diagonal()
    resultat = summe_prufen(diagonal2)
    if resultat == 1:
        eins = True
    elif resultat == 2:
        zwei == True

    print(zwei)
    if eins == True and zwei == True:
        return 0
    elif eins == True:
        return 1
    elif zwei == True:
        return 2
    else:
        boolean_array = board > 0
        if np.sum(boolean_array) < 9:
            return -1
        else:
            return 0

def check_uniform(line,gesamtsumme):
    if gesamtsumme == 3:
        boolean_arr = (line == 1)
        gesamtbetrag = np.sum(boolean_arr)
        if gesamtbetrag == 3:
            return 1

    elif gesamtsumme == 6:
        boolean_arr = (line == 2)
        gesamtbetrag = np.sum(boolean_arr)
        print(gesamtbetrag)
        if gesamtbetrag == 3:
            return 2

def summe_prufen(line):
    gesamtsumme = np.sum(line)
    if gesamtsumme == 3 or gesamtsumme == 6:
        uniform = check_uniform(line, gesamtsumme)
        return uniform
    else:
        return 0
