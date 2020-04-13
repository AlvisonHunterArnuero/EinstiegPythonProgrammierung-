# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if len(str) > 1:
      first = str[0]
      last = str[-1]
      mid = str[1:len(str)-1]
      return print(last + mid + first)
    else:
      return print (str)


#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
# the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
    if len(str) >3:
        rpt = str[0:3]
        return print(rpt + rpt + rpt)
    else:
        return print (str + str + str)


front_back('tomato')
front3("Chocolate")

