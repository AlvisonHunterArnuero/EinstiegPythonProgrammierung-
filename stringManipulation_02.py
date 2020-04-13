#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
# the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
    if len(str) >3:
        rpt = str[0:3]
        return print("The new string results are: ", rpt + rpt + rpt)
    else:
        return print ("New String is: ", str + str + str)

front3("Chocolate")
front3("era")
front3("Chespirito")



