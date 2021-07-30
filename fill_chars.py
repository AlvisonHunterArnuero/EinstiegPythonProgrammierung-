# Made with ❤️ in Python 3 by Alvison Hunter - February 20th, 2021
def fillChar(desired_char, iter):
    counter = 0
    for el in range(1,iter):
        if(el>2):
            counter+=1
            pat = " "*counter
            print(f"{desired_char}{pat}{desired_char}")
        else:
            print(f"{desired_char*el}")

    print(f"{desired_char*iter}")

fillChar("*",6)

