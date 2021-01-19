# Made with ❤️ in Python 3 by Alvison Hunter - December 31st, 2020
def find_solution(string,markers):
    lst_temp = string.split("\n")
    for index_num,elem in enumerate(lst_temp):
        for marker in markers:
            if(elem.find(marker) != -1):
                lst_temp[index_num] = elem[:elem.find(marker)].strip()
                break

    print("\n".join(lst_temp))
    print('-'*65)
    return("\n".join(lst_temp))

find_solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# "apples, pears\ngrapes\nbananas"
find_solution("a #b\nc\nd $e f g", ["#", "$"]) # "a\nc\nd"
# 'avocados lemons avocados oranges strawberries\n\nwatermelons cherries avocados strawberries'
find_solution('avocados lemons avocados oranges strawberries\n.\nwatermelons cherries avocados strawberries',['#', "'", '.', '!', ',', '^'])
find_solution("! pears avocados oranges\nstrawberries cherries lemons lemons cherries watermelons\n' - oranges oranges\ncherries ! bananas bananas strawberries\noranges cherries cherries", ['-', "'", '!', '@', '^'])
