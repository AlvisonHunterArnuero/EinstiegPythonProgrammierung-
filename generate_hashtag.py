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


generate_hashtag('')# False, 'Expected an empty string to return False')
generate_hashtag('Do We have A Hashtag')#[0], '#', 'Expeted a Hashtag (#) at the beginning.')
generate_hashtag('Codewars')# '#Codewars', 'Should handle a single word.')
generate_hashtag('Codewars      ')# '#Codewars', 'Should handle trailing whitespace.')
generate_hashtag('Codewars Is Nice')# '#CodewarsIsNice', 'Should remove spaces.')
generate_hashtag('codewars is nice')# '#CodewarsIsNice', 'Should capitalize first letters of words.')
generate_hashtag('CodeWars is nice')# '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
generate_hashtag('c i n')# '#CIN', 'Should capitalize first letters of words even when single letters.')
generate_hashtag('codewars  is  nice')# '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
