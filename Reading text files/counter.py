fichier = open("mbox-short.txt")
count = 0
for lx in fichier:
    lx = lx.rstrip()
    if lx == "": continue
        
    words = lx.split()
    if words[0] !="From": continue
        
    print(words[1])
    count = count+1

print ("There were", count, "lines in the file with From as the first word")
