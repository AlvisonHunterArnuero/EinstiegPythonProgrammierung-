# Exercise number 1
import random
max_num = 0
position = 0
rand_lst = []
mayor_dict = {}
for el in range(20):
    num_rnd = random.randint(1, 99)
    rand_lst.append(num_rnd)

max_num = max(rand_lst)
position = rand_lst.index(max_num)
mayor_dict['Valor'] = max_num
mayor_dict["Posicion"] = position
print(mayor_dict)
