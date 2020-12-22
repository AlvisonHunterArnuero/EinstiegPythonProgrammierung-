# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal: It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Made with ❤️ in Python 3 by Alvison Hunter - December 2nd, 2020
import re
def generate_hashtag(str):
    if(len(str)>140 or str == ''):
        return False
    else:
        tmp_str = re.sub('[\s+]', '', str.title())
        str = "#"+tmp_str
        print(str)
        return str

#This is a set of scenarios that we will use on this particular challenge
generate_hashtag('')# False, 'Expected an empty string to return False')
generate_hashtag('Do We have A Hashtag')#[0], '#', 'Expeted a Hashtag (#) at the beginning.')
generate_hashtag('Nicaragua')# '#Nicaragua', 'Should handle a single word.')
generate_hashtag('Nicaragua      ')# '#Nicaragua', 'Should handle trailing whitespace.')
generate_hashtag('Nicaragua Is Wonderful')# '#NicaraguaIsWonderful', 'Should remove spaces.')
generate_hashtag('Nicaragua is wonderful')# '#NicaraguaIsWonderful', 'Should capitalize first letters of words.')
generate_hashtag('Nicaragua is Wonderful')# '#NicaraguaIsWonderful', 'Should capitalize all letters of words - all lower case but the first.')
generate_hashtag('c i n')# '#CIN', 'Should capitalize first letters of words even when single letters.')
generate_hashtag('nicaragua  is  wonderful')# '#NicaraguaIsWonderful', 'Should deal with unnecessary middle spaces.')
