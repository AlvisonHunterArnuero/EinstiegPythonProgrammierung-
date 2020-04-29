from math import factorial
 
def print_permutations_lexicographic_order(s):
    """Print all permutations of string s in lexicographic order."""
    seq = list(s)
 
    # there are going to be n! permutations where n = len(seq)
    for _ in range(factorial(len(seq))):
        # print permutation
        print(''.join(seq))
 
        # find p such that seq[p:] is the largest sequence with elements in
        # descending lexicographic order
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1
 
        # reverse seq[p:]
        seq[p:] = reversed(seq[p:])
 
        if p > 0:
            # find q such that seq[q] is the smallest element in seq[p:] such that
            # seq[q] > seq[p - 1]
            q = p
            while seq[p - 1] > seq[q]:
                q += 1
 
            # swap seq[p - 1] and seq[q]
            seq[p - 1], seq[q] = seq[q], seq[p - 1]
 
 
s = input('Enter the string: ')
print_permutations_lexicographic_order(s)
