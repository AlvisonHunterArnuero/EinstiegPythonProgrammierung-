filename = input("Enter file name: ")
filehandler = open(filename)
lst = list()
for lx in filehandler:
    lx=lx.rstrip()
    lx= lx.split()
    for c in lx:
        print(c)
        if c in lst:
           continue
        else:
           lst.append(c)
            
lst.sort()
print(lst)
