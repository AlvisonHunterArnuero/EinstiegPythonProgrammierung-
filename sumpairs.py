arrNumbers = [10,20,20,10,10,30,50,10,20]
arrRes = {} 
totalPairs = 0 
for item in arrNumbers: 
  if (item in arrRes):
      arrRes[item] += 1
  else:
   arrRes[item] = 1
   
for z, w in arrRes.items(): 
 totalPairs += int(w/2) 
print(f" The sum of all pairs is : {totalPairs}.")
