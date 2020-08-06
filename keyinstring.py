string = input("Enter a long string \n") 
key = input("Enter the letter to search for: \n")
if(key in string):                  #Checks if key is in the string
    print("Letter found in string") #If the Bool value is TRUE
else:
    print("Letter not found in string \n")
input("Press enter \n")
