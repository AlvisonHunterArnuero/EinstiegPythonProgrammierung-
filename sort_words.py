def sort_words():
    phrase = input("Please enter your words: \n")
    words = phrase.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    sortedString = ' '.join(words)
    return print(f"Sorted Phrase by words is: \n {sortedString}")

sort_words()
