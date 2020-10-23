# How to get a multiline input from user in Python?
# Made with ❤️ in Python 3 by Alvison Hunter - Saturday, October 17th, 2020
def multi_input():
    try:
        #This list will hold all inputs made during the loop
        lst_words = []
        # We will store the final string results on this variable
        final_str =''
        #Let's ask first the user to enter the amount of fruits
        print("Please Type in your List of Fruits. \n Press << Enter >> to finish the list:")

        #Loop to get as many words as needed in that list
        while True:
            #Capture each word o'er here, pals!
            wrd = input()
            # If word is empty, meaning user hit ENTER, let's break this routine
            if not wrd: break
            # if not, we keep adding this input to the current list of fruits
            else:
                lst_words.append(wrd)

#What if ther user press the interruption shortcut? ctrl+D or Linus or MacOS equivalent?
    except KeyboardInterrupt:
        print("program was manually terminated by the user.")
        return
#the time has come for us to display the results on the screen
    finally:
        #If the list has at least one element, let us print it on the screen
        if(len(lst_words)>0):
            #Before printing this list, let's create the final string based on the elements of the list
            final_str = '\n'.join(lst_words)
            print('You entered the below fruits:')
            print(final_str)
        else:
            quit
#let us test this function now! Happy python coding, folks!
multi_input()
