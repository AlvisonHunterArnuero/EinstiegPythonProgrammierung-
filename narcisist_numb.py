#Made with ❤️ in Python 3 by Alvison Hunter - October 4th, 2020
def narcissistic(value):
    try:
        #sum_powers will store the results of each iteration
        sum_powers = 0

        #iterate through each character of the param
        for elem in str(value):
            #add the results of the elevated character to sum_powers
            sum_powers += int(elem)**int(len(str(value)))

    except:
        print("Uh oh! Something went really wrong!")
        quit
    # if all went well, the time has come to print the results
    finally:
        if (sum_powers == value):
            print(str(value), ' is narcissistic')
            return True
        else:
            print(str(value), ' is not narcissistic')
            return False

narcissistic(153)

