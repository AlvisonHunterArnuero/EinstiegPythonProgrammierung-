# Bob is preparing to pass IQ test. The most frequent task in this test is to find out
# which one of the given numbers differs from the others. Bob observed that one number
# usually differs from the others in evenness. Help Bob — to check his answers,
# he needs a program that among the given numbers finds one that is different in evenness,
# and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes
# of the elements start from 1 (not 0)
# ##Examples :
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
# Made with ❤️ in Python 3 by Alvison Hunter - December 3rd, 2020
def iq_test(numbers):
    oddlst = []
    evenlst = []
    list_difference = []
    numblst = numbers.split()
    numblst = [int(i) for i in numblst]
    for n in numblst:
        if n % 2 > 0:
            oddlst.append(n)
        else:
            evenlst.append(n)

    if(len(oddlst)>len(evenlst)):
        print(numblst)
        for item in numblst:
            if item not in oddlst:
                list_difference.append(item)

        print('Index is ',(numblst.index(list_difference[0])+1))
    else:
        for item in numblst:
            if item not in evenlst:
                list_difference.append(item)

        print('Index is ',(numblst.index(list_difference[0])+1))

    print(list_difference)

iq_test("2 4 7 8 10")
iq_test("1 2 1 1")
