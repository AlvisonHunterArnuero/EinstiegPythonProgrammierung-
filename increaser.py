rng = range(1,9)
sum = 0
increaser = 4
result = 0
for rng_num in rng:
    result = result + (rng_num + increaser)
    print(f"{rng_num} + {increaser} = {result}")
    increaser = increaser +1
