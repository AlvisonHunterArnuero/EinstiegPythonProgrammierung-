from itertools import permutations


def permutations(given_str):
    if len(given_str) == 1:
        return list(given_str)

    elif len(given_str) == 2:
        str = (given_str + " " + given_str[::-1]).split()
        return list(set(str))

    permutazione_ricorsiva = set()
    for elem in given_str:
        for perm in permutations(given_str.replace(elem, '', 1)):
            permutazione_ricorsiva.add(elem+perm)

    final_perms_lst = set(permutazione_ricorsiva)
    return list(final_perms_lst)


print(permutations('a'))  # ['a'])
print(permutations('ab'))  # ['ab', 'ba'])
print(permutations('aa'))  # ['ab', 'ba'])
print(permutations('aabb'))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
