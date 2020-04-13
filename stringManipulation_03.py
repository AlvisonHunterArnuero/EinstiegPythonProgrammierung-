# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    if str[0:3] .upper()== "NOT":
        return print(str)
    else:
        return print("Not "+str)

not_string('War dogs')
not_string('a Minute to pray')
not_string('Not for cowards')

