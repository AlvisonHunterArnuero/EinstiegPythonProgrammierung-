# --------------------------------------------------------------------------------
# Introduction to list iterations with several procedures, aiming to the same result.
# Made with ❤️ in Python 3 by Alvison Hunter - March 17th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------

# Using a for loop to extract the data
demo_lst = [2098, 3456, 5432, 5678]
for elem in demo_lst:
    print(elem)

print("-"*40) # This is just a divider

# Combining for loop with the Enumerate method to get current index.
cities_lst = ["Madrid","Managua", "Paris", "Londres"]
for ind, city in enumerate(cities_lst):
    print(f"{str(ind+1)} - {city}")

print("-"*40) # This is just a divider

# Using the Range method
spoken_languages_lst = ["English","Spanish", "French", "Italian", "German"]
for lang in range(len(spoken_languages_lst)):
    print(f"• {spoken_languages_lst[lang]}")

print("-"*40) # This is just a divider

# Using list comprehension to iterate through the list
best_players_lst = ["Cristiano Ronaldo", "Lionel Messi","Kylian Mbappé","Mohamed Salah"]
[print(f"{inx+1} - {el}") for inx, el in enumerate(best_players_lst)]
