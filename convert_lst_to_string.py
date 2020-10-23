#Convert List to String with 4 simple methods, nothing fancy :)
# Made with ❤️ in Python 3 by Alvison Hunter - October 12th, 2020

# Method 1 - We will use a function to convert this list to string
def listToString(listArg):
    result_string = ""
    for elem in listArg:
        result_string = result_string+' ' + elem

    print('Method #1: ', result_string)
#-------------------------------------------------------------------
# Method #2: Using .join() method to accomplish this task
def listToStringJoin(lst_arg):
    res_str = " "
    print('Method #2: ', res_str.join(lst_arg))
#-------------------------------------------------------------------
# Method #3: Using list comprehension
def listToStringLstComprehension(lst_args):
    listToStringResult = ' '.join([str(elem) for elem in lst_args])
    print('Method #3: ',listToStringResult)
#-------------------------------------------------------------------
# Method #4: Using map()
def listToStringMap(lstArgs):
    lst_to_str_res = ' '.join(map(str, lstArgs))
    print('Method #4: ',lst_to_str_res)

# we will use these lists to test these methods
sampleList = ['CR7', 'is', 'the','greatest','football','player','of','the','world']
mixedTypeList = ['I know','some python,',2, 'JS Frameworks', 'and', 1, 'JS Library']

# Let's try this with the four methods,
listToString(sampleList) #call method 1
listToStringJoin(sampleList) #call method 2
listToStringLstComprehension(mixedTypeList) #call method 3
listToStringMap(mixedTypeList) #call method 4

