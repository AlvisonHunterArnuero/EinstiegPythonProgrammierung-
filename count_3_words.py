from collections import Counter
import re
import string as s


def top_3_words(text):
    if len(text) > 0:
        sep_text = re.sub(r"[^ a-zA-Z']", "", text.lower()).split()
        wrd_cnt = Counter(sep_text)
        final_lst = sorted(wrd_cnt, key=wrd_cnt.__getitem__, reverse=True)[: 3]
        print(final_lst)
    else:
        print([])



# ["e", "d", "a"]
top_3_words("a a a  b  c c  d d d d  e e e e e")
# ["e", "ddd", "aa"]
top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# ["won't", "wont"]
top_3_words("  //wont won't won't ")
# ["e"]
top_3_words("  , e   .. ")
# []
top_3_words("  ...  ")
# []
top_3_words("  '  ")
# []
top_3_words("  '''  ")

# ["a", "of", "on"]
top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""")
