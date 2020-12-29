# Given a string, return a new string where the first and last chars
# have been exchanged.
def front_back(str):
    if len(str) > 1:
      first = str[0]
      last = str[-1]
      mid = str[1:len(str)-1]
      return print(last + mid + first)
    else:
      return print (str)
front_back('tomato')
