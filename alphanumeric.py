import re
# using the isalnum() funct could fix this issue but it is all about practicing so,
# lets do it the Nica way, by doing this manually to learn from scratch

def alphanumeric(password):
    if(password=="" or password==None):
        print('This string is Empty and therefore false')
        return False

    if(re.match('^[a-zA-Z0-9]+$',password,0)):
        print("This is True")
        return True
    else:
        print("This is Not True")
        return False

#Let us test this out, folks
alphanumeric("345TT^Y")
alphanumeric("6789YU_")
alphanumeric("")
alphanumeric("ADFGTYtyterw")




