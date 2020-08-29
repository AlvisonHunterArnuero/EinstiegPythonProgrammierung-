file_name = input("Enter file:")
if len(file_name) < 1 : file_name = "mbox-short.txt"
file_handler = open(file_name)

lst = list()

for ln in file_handler:
    if not ln.startswith("From:"): continue
    ln = ln.split()
    lst.append(ln[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
