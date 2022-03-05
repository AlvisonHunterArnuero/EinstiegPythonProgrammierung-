# ----------------------------------------------------------------------------
# Return True if first letter of msg is equals to last. True if msg is empty
# Made with ❤️ in Python 3 by Alvison Hunter - February 6th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ----------------------------------------------------------------------------

def first_and_last(msg):
    return True if len(msg)==0 else (msg[0]==msg[-1])

#Test Cases, using the examples given on the FB post
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))