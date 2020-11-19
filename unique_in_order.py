def unique_in_order(iterable):
        lst_iterable =list(iterable)
        for el in range(len(lst_iterable)):
                next_el = lst_iterable[el+1]
                if ( lst_iterable[el] == next_el):
                        print(lst_iterable[el] , ' is equal to ', next_el)
                        lst_iterable.remove(next_el)
                        print('Final lisrt',lst_iterable)
                        

unique_in_order('AAAABBBCCDAABBB')# == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD') #        == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])#       == [1,2,3]
