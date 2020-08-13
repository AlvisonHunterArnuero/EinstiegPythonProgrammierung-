# Made with ❤️ in Python 3 by Alvison Hunter - June 21th, 2020
def get_prime_factors():
        num=int(input("Please Enter Your Number: \n"))
        factors = list()
        divisor = 2
        while(divisor <= num):
            if(num % divisor) == 0:
                factors.append(divisor)
                num = num/divisor
            else:
                divisor +=1
        return print(f"Prime Factors List: \n{factors}")

get_prime_factors()
