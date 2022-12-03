# ---------------------------------------------------------------------------
# Python List Cheatsheet - Basic Examples with the most common methods
# Made with ❤️ in Python 3 by Alvison Hunter - July 14th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------

# First, we will need a list of animals, to play with it
dummy_emojis = ['🐮','🐷','🐷','🦊']

# Let's add an item to the existing list
dummy_emojis.append('🐵')
print(dummy_emojis)

# Copy the list to another one
new_dummy = dummy_emojis.copy()
print(new_dummy)

# Where the heck is the monkey? let's find out
print(f"🐵 was found at {dummy_emojis.index('🐵')} position")

# How many pigs do we have in this list? let's count them
print('🐷 = ',dummy_emojis.count('🐷'))

# Add a doggie on this list, at index 3
dummy_emojis.insert(3,'🐶')
print(f"🐶 was inserted on {dummy_emojis}")

# Let's take the first pig out, with pop!
dummy_emojis.pop(1)
print(f"🐷 was removed from {dummy_emojis}")

# let's remove the cow on this list, ok?
dummy_emojis.remove('🐮')
print(f"🐮 was removed from {dummy_emojis}")

# Let's apply a reverse order on this list, shall we?
dummy_emojis.reverse()
print('Reversed List: ', dummy_emojis)
