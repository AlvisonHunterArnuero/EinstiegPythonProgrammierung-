# Made with ❤️ in Python 3 by Alvison Hunter - December 28th, 2020
def get_prime_numbers(upper):
    try:
        for num in range(2, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return
                    else:
                        print(num)
    except:
            print('Uh oh, something went terribly wrong!')
    finally:
        print('Thanks')

get_prime_numbers(5)
