# def scramble(s1, s2):
#     try:
#         lst01 = list(s1)
#         for el in s2:
#             if(el in s1):
#                 lst01.pop(lst01.index(el))
#             else:
#                 return False
#         return True
#     except ValueError:
#         return False


def scramble(s1, s2):
    for el in set(s2):
        if s1.count(el) < s2.count(el):
             print(False)
    print(True)



print(scramble('rkqodlw', 'world'))  # True
print(scramble('cedewaraaossoqqyt', 'codewars'))  # True
print(scramble('katas', 'steak'))  # False
print(scramble('scriptjava', 'javascript'))  # True
print(scramble('scriptingjava', 'javascript'))  # True
