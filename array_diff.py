# Your goal in this kata is to implement a difference function, which subtracts
# one list from another and returns the result.
# It should remove all values from list a, which are present in list b.
# Made with ❤️ in Python 3 by Alvison Hunter - Saturday, October 19th, 2020
def array_diff(lst_01, lst_02):
    cnt = 0
    if not lst_01:
        print('First list has no elements: ', lst_01)
        return []
    elif not lst_02:
        print('Second list is empty. Returning first list: ', lst_01)
        return lst_01
    else:
        while cnt < len(lst_01):
            for elem in lst_02:
                if(elem in lst_01):
                    lst_01.remove(elem)
            cnt +=1

        print(lst_01)
        return lst_01

#let us test this out with some scenarios, dear Pythonistas and pythoneers!
array_diff([1,2], [1]) # [2], "a was [1,2], b was [1], expected [2]")
array_diff([1,2,2], [1]) # [2,2], "a was [1,2,2], b was [1], expected [2,2]")
array_diff([1,2,2], [2]) # [1], "a was [1,2,2], b was [2], expected [1]")
array_diff([1,2,2], []) # [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
array_diff([], [1,2]) # [], "a was [], b was [1,2], expected []")


