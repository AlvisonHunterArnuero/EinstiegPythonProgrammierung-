filename = input("Enter file:")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)
d=dict()
for lx in handle:
    if not lx.startswith("From "): 
        continue
    else:    
        lx=lx.split()
        lx=lx[5]
        lx=lx[0:2]
        d[lx]=d.get(lx,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)
