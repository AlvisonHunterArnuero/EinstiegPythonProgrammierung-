# -----------------------------------------------------------------------
# Python Tricks and tips for better coding -Basic Python coding
# Made with ❤️ in Python 3 by Alvison Hunter - November 19th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -----------------------------------------------------------------------

# Declare function params with default values
def draw_pattern(single='*', triple=' ',amount=3):
  
    # First, create a pattern to be repeated
    pattern = f'{single}{triple*amount}'
    
    # Add this pattern to the result string
    result = f'{pattern*amount}{single}'
    
    # Print the results of this string concatenation
    print(result)
    
# Now is time to repeat these patterns with
# a for loop calling the function twice
for i in range(2):
    draw_pattern('*','-')
    draw_pattern('|',' ')
    
# To seal the deal, let's replicate
# the first pattern in the last row
draw_pattern('*','-')