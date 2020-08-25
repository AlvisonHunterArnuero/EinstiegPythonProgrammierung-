# This routine finds how many uppercase characters, lowercase characters
# and amount of digits we have on the given string entered by the user
# we use a list to put all these matches and then if is successful,
# we print it on the screen, otherwise print unsuccessful

# Made with ❤️ in Python 3 by Alvison Hunter - April 24th, 2020
import re
def main():
    string = input("Please type in your string: ")
# we declare the patterns that we will use to perform
# this search in every case given above
    textuppercase = '[A-Z]'
    textlowercase = '[a-z]'
    numerical = '[0-9]'

# Now let's use a list to put all of these results on it for printing it on the screen
    results_list = [len(re.findall(textlowercase, string) ),
                    len(re.findall(textuppercase, string) ),
                    len(re.findall(numerical, string) )]

# Let's confirm if the object is actually empty or if it has content,
# if so, let us print it on the screen now
    if results_list:
      print(f"Search successful. The list now contains the results like this:  {results_list}")
      print(f"Lowercase: {results_list[0]} \nUppercase: {results_list[1]} \nDigits: {results_list[2]}")
    else:
      print("Search unsuccessful. Please try with another string.")

if __name__ == "__main__":
    main()
