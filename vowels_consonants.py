# ------------------------------------------------------------------------------------
# Write a python program that gets a phrase and save all vowels and consonants
# in 2 separate lists that should not contain repeated letters. print them afterwards.
# ------------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - February 28th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ------------------------------------------------------------------------------------

def get_alpha_chars():
    try:
        vowels = "AaEeIiOoUu"
        vowels_lst = []
        consonants_lst = []

        # Get the phrase from the user input
        phrase = input("Please enter your phrase: \n")
        # let us clean the entered phrase
        cleaned_phrase = set(''.join(ch for ch in phrase if ch.isalpha()))

        # let  us start by iterating the set we recently built
        for letter in cleaned_phrase:
            vowels_lst.append(letter) if letter in vowels else consonants_lst.append(letter)

        # Print the results now
        print(f"Vowels: {vowels_lst}" if vowels_lst else "No Vowels found")
        print(f"Consonants: {consonants_lst}" if consonants_lst else "No Consonants found")
    except:
        print("Uh Oh! An unexpected error has occurred. Please try again later.")
        quit()

# Call the declared function now, folks
get_alpha_chars()
