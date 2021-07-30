# --------------------------------------------------------------------------------
# You will be given a vector of strings. You must sort it alphabetically
# (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.
# --------------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - March 23th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
def two_sort(array):
    str_result = ""
    tmp_list ="***".join(list(sorted(array)[0]))
    print(tmp_list)


two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]) # 'b***i***t***c***o***i***n' )
two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]) # 'a***r***e')
two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]) # 'a***b***o***u***t')
two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]) # 'c***o***d***e')
two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]) # 'L***e***t***s')
