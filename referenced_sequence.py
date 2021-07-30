# --------------------------------------------------------------------------------
# Introduction to list iterations with several procedures, aiming to the same result.
# Made with ❤️ in Python 3 by Alvison Hunter - March 17th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------

# si quiero que sean 3 posiciones seria
# [1,1,1,4,4,4,7,7,7,10,10,10,12,12]
ref_lst = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def reference_by_position(seq, num):
    avg = len(seq) / float(num)-1
    out = []
    tmp = []
    last = 0.0

    while last < len(seq):
        try:
            if num<=0:
                print("Number has to be greater that 1.")
                quit
            out.append(seq[int(last):int(avg)])
            last = avg
            avg +=3
        except ValueError:
            print("Uh oh! You should've entered an integer number!")
            quit
        except ValueError:
            print("An unexpected error has occured!")
            quit

    return out


print(reference_by_position(ref_lst, 3))







