import numpy as np
data = [
    150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000]

mean = np.mean(data)
print("MEAN:", mean)
sd = np.sqrt(np.var(data))
print("STANDARD:", sd)
cntr = 0
for y in data:
    if y >= (mean-sd) and y <= (mean+sd):
        cntr += 1
print((cntr/len(data))*100)
