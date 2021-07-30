# Made with ❤️ in Python 3 by Alvison Hunter - December 31st, 2020
def find_solution(string, markers):
    lst_rows = string.split("\n")
    for index_num, elem in enumerate(lst_rows):
        for marker in markers:
            ind = elem.find(marker)
            if (ind != -1):
                elem = elem[:ind]
                lst_rows[index_num] = elem.rstrip(' ')

    print("\n".join(lst_rows))
    print('-'*65)
    return("\n".join(lst_rows))


find_solution("apples, pears\ngrapes\nbananas !", ["#", "!"])
find_solution(
    "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# "apples, pears\ngrapes\nbananas"
find_solution("a #b\nc\nd $e f g", ["#", "$"])  # "a\nc\nd"
# 'avocados lemons avocados oranges strawberries\n\nwatermelons cherries avocados strawberries'
find_solution('avocados lemons avocados oranges strawberries\n.\nwatermelons cherries avocados strawberries', [
              '#', "'", '.', '!', ',', '^'])
find_solution("! pears avocados oranges\nstrawberries cherries lemons lemons cherries watermelons\n' - oranges oranges\ncherries ! bananas bananas strawberries\noranges cherries cherries",
              ['-', "'", '!', '@', '^'])
