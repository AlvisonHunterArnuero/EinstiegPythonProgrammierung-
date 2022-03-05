arr = [1,2,3,4,5,6,7,8,9,10]
str_res = ""
print("x",','.join(map(str, arr)))
for el in arr:
    str_res = ""
    for elem in arr:
        str_res += " "+str(el*elem).zfill(2)


    print(str(el).zfill(2), str_res)
