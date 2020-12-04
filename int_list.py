# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 >> [5,4,3,2,1]
# Made with ❤️ in Python 3 by Alvison Hunter - December 2nd, 2020

def reverse_seq(n):
    return sorted([ x for x in range(1,n+1)], reverse=True) if n>0 else None

#let us call the function here now.    
reverse_seq(15)
