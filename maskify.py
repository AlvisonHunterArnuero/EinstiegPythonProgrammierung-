# return masked string from a given number passed as param
# Made with ❤️ in Python 3 by Alvison Hunter - October 5th, 2020
def maskify(cc_numb):
    try:
        masked_str = cc_numb
        if len(cc_numb)>4:
            masked_str ="#" * (len(cc_numb)-4) + cc_numb[-4:]
    except:
        print("Uh oh! Something went really wrong!")
        quit
    finally:
        print('Credit Card Masked Numbers: ',masked_str)
        return masked_str

maskify('3442345') 

