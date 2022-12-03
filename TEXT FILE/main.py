with open('data.txt') as f:
    lines_lst = [[line.strip().split()] for line in f.read().splitlines()]
    [lines_lst.remove(el) for el in lines_lst if el ==""]
    # 12/JUL/2022 11:15 MOVIST 81482911 02:18 16.54
    lst =[]
    
    print(f'TOTAL EN LLAMADAS C$: {sum([float(t[0][5]) for t in lines_lst])}')
    print("DIA/MES/AÑO| HORA | NUMERO | MINS | C$ ")
    [print(f"{l[0][0]} {l[0][2]} {l[0][3]} {l[0][4]} {l[0][5]}") for l in lines_lst]
    print('The count of the numbers is ',  len(lines_lst))
