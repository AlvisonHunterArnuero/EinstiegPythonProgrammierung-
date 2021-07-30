# -------------------------------------------------------------------------
# Basic operations with colletion types | Python exercises | Beginner level
# Apply reverse(), sorted() & sort() list method on a given list
# Made with ❤️ in Python 3 by Alvison Hunter Arnuero - May 12th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
lst = [6, 1, 2, 7, 4, 8, 3, 9, 5]
lst2 = ['A', 'U', 'G', 'A', 'R', 'A', 'C', 'I', 'N']

# Display both lists with their initial order & elements
print(f"FIRST: {lst} \nSECOND: {lst2}")

# Call the reverse method on this list
lst.reverse()
# Displaying the list once is sorted
print(f"FIRST LIST REVERSED: {lst}")

# Sorting the original first list
print(f"FIRST LIST SORTED: {sorted(lst)}")

# Less traditional solution
print(f"SECOND LIST REVERSED: {lst2[::-1]}")

# Sorting the original second list with the sort method
lst2.sort()
print(f"SECOND LIST SORTED: {lst2}")

# We could sort and reverse a list as well in a whole sentence
lst.sort(reverse=True)
print(f"FIRST LIST SORTED & REVERSED: {lst}")
