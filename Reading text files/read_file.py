# Use the file name mbox-short.txt as the file name
fichier = input("Please enter file name: ")
fh = open(fichier)
count = 0
avg = 0
for lx in fh:
    if not lx.startswith("X-DSPAM-Confidence:") : continue
    avg += float(lx[20:-1].strip())
    count = count + 1
    
print("Average spam confidence:", (avg/count))
