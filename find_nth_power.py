import math as m
def index(array, n):
    response = None
    try:
        response  = m.pow(array[n],n)
        print(str(response).rstrip('0').rstrip('.'))
        return response
    except:
        print("Oh uh, an Error has ocurred: Index out of Range")
        return -1
# lambda a, n: -1 if len(a)<=n else a[n]**n
index([1, 2, 3, 4],2) # 9
index([1, 3, 10, 100],5) # 1000000
