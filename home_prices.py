lst_homes = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
             {'año': 2012, 'metros': 60, 'habitaciones': 2,
                 'garaje': True, 'zona': 'B'},
             {'año': 1980, 'metros': 120, 'habitaciones': 4,
                 'garaje': False, 'zona': 'A'},
             {'año': 2005, 'metros': 75, 'habitaciones': 3,
                 'garaje': True, 'zona': 'B'},
             {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def search_home(lst, price):
    tmp_lst = []
    precio = 0
    for n, el in enumerate(lst):
        if(el.get('zona') == "A"):
            print(el.get('zona'))
            precio = (metros * 1000 + habitaciones * 5000 +
                      garaje * 15000) * (1-antiguedad/100)

        else:
            precio = (metros * 1000 + habitaciones * 5000 +
                      garaje * 15000) * (1-antiguedad/100) * 1.5

    print(precio)

    # precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)


search_home(lst_homes, 2000)
