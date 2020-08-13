myPets = ['Kiki', 'Brownie', 'Gringo']

#Let us start by getting the Pet's name on this sentence
myPetName= input("What is your Pet's Name?\n")

#As long as the user keeps  typing the wrong name, the
# routine will keep asking for your pet's name,
# for the example we will use the name "Kiki"
while myPetName != 'Kiki':
    print(f"I do not have a pet named {myPetName}.")
    #Now, let's ask one more time your pet's name.   
    myPetName= input("What is your Pet's Name?\n")

# Now that the user types in the right name of your pet
# in this case we are using Kiki, let's print it on the screen
print(f"{myPetName} is certainly the name of my pet.")


