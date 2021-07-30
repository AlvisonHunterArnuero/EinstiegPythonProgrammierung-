from collections import Counter
import operator
most_rep_c = ""
f = open("phrases.txt", "r")
output = f.readline()
f.close()
phrase = output.replace(" ", "")
print(phrase)
new_dict = dict(Counter(phrase))
most_rep_c = max(new_dict.items(), key=operator.itemgetter(1))[0]
print(f"Most repeated character is {most_rep_c} with {new_dict[most_rep_c]} repetitions.")
