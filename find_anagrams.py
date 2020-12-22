# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.
# For example:
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
# Made with ❤️ in Python 3 by Alvison Hunter - December 7th, 2020
def anagrams(word1, wordlist):
    # This list will contain the anagrams found on the process
    final_list = []
    # First, let us validate is the word is alpha and case it to lower
    word1 = [c for c in word1.lower() if c.isalpha()]
    # Sort it to make the comparisons with the other words in the list
    word1 = "".join(sorted(word1))

    # It is time to do the same with the list elements, each word separately
    for w in wordlist:
        # Validate is the word is alpha and case it to lower
        w = [c for c in w.lower() if c.isalpha()]
        # Temp string to concatenate the inicial word not sorted
        # This will be used to add it to the final list if is equal to word1
        str1 = ""
        initword = str1.join(w)
        # Now we sort the list element to compare it to word1
        w = "".join(sorted(w))
        # If they are the same, we add them to the final list of anagrams
        if(w==word1):
            final_list.append(initword)
            print(final_list)

    # We print on the screen the final list and return it afterwards
    print(f'Array Final: {final_list}\n')
    return(final_list)
  
# Time to run some examples of this solution and drink some coffee afterwards
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) #=> ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #=> ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) #=> []
