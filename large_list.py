
large_list =[['maj', 4, 7], ['3', '5'], ['maj9', 7], ['maj3', 100], ['maj4', 1360], ['maj7', 4, 7, 11], ['3', '5', '7']]
def getTheMinGuy(mylist):
    minimum = min(mylist)
    return print(f"The smaller sublist on this list is => {minimum}")
getTheMinGuy(large_list)
