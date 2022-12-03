# ---------------------------------------------------------------------------
# PYTHON CODING CHALLENGE - RIGHT PERSON FOR JOB
# Connect right person with their favorite kind of data/table
# Eric Likes numbers. John likes strings and Terry likes mixes
# output:
# "Eric has [23,31,56,24,42]"
# "John has ['France','United States','Bangladesh','Brazil']"
# "Terry has ['Paris',16,'New York',5,'Dhaka',17, 'Rio', 'Ipanema']"
# ---------------------------------------------------------------------------
# Made with ❤️ in Python 3 by Alvison Hunter - August 9th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------

input = [
    [23, 31, 56],
    ["France", "United States"],
    ["Paris", 16, "New York", 5],
    ["Bangladesh", "Brazil"],
    [24, 42],
    ["Dhaka", 17, "Rio", "Ipanema"],
]

def person_connector(given_lst):
    eric_lst = []
    john_lst = []
    for i, lst in enumerate(given_lst):
        if all(isinstance(el, int) for el in lst):
            for item in lst:
                eric_lst.append(item)
            given_lst.pop(i)

    for i, lst in enumerate(given_lst):
        if all(isinstance(el, str) for el in lst):
            for elem in lst:
                john_lst.append(elem)
            given_lst.pop(i)

    terry_lst = [item for sublist in given_lst for item in sublist]
    final_msg = f"Erick has {eric_lst} \nJohn has {john_lst}\nTerry has{terry_lst}"
    return final_msg


right_person_4_job = person_connector(input)
print(right_person_4_job)
