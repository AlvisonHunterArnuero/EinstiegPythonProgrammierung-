def countOnes(links, rechts):
    d = rechts
    top_recht = 0
    while rechts:
        top_recht += 1
        rechts = round(rechts/2)
    boot_list = [0,1]
    for i in range(top_recht):
        boot_list += [x+1 for x in boot_list]
    results = sum(boot_list[links:d+1])
    print(results)

countOnes(4,7) # 8
countOnes(5,7) # 7
countOnes(12,29) #51
