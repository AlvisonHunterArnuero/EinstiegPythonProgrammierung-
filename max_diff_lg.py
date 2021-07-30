# Made with ❤️ in Python 3 by Alvison Hunter - January 20th, 2021
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    else:
        final_results = max([len(sorted(a1, key=len)[-1]) - len(sorted(a2, key=len)[0]),len(sorted(a2, key=len)[-1]) - len(sorted(a1, key=len)[0])])
        print('Results: ',final_results)
        return final_results

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) # 13
