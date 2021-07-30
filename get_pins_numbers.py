from itertools import product as pd


def get_pins(observed):
    NUMPAD_NABR = ('08', '124', '2135', '326', '4157',
                   '52468', '6359', '748', '85790', '968')
    adjoiners = [NUMPAD_NABR[int(n)] for n in observed]
    adjointed_lst = list(pd(*adjoiners))
    pers_id_num_comb = [''.join(r) for r in adjointed_lst]
    return(pers_id_num_comb)


print(get_pins('8'))  # ['5','7','8','9','0'])
#["11", "22", "44", "12", "21", "14", "41", "24", "42"]
print(get_pins('11'))
