#-------------------------------------------------------------------------------------------------------
#               Made with ❤️ in Python 3 by Alvison Hunter Arnuero - February 2nd, 2022
#               JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
#-------------------------------------------------------------------------------------------------------

num_lst =["1","2","3","22","232"]

# Declare function to expect two parameters to proceeed with this: Trigger string being targeted and the
# list of numbers. We've also declare default params just in case these are not being provided.
def get_trigger(trg="1", lst=[]):
    return ("No data provided", [elem for elem in lst if trg in elem])[True if len(lst) > 0 else False]

# Print the function results, don't forget to pass the parameters
print(get_trigger("2",num_lst))

# If you forget to pass params, we will handle it like this
print(get_trigger())