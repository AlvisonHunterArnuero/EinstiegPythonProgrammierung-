def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            res = False if (num % i == 0) else True
            print(res)
        return res

def app():
    num = int(input('Write a number: '))
    result = isPrime(num)

    if result is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')

if __name__ == '__main__':
    app()
