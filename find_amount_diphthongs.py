# --------------------------------------------------------------------------------
# Find the amount of diphtongs in a sentence and the word containing the diphtong.
# Made with ❤️ in Python 3 by Alvison Hunter - March 15th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------
diphthongs = ['ua', 'ue', 'uo','ia','ie', 'io','ai','ei','oi','au','eu','ou','iu','ui']
Sentence = """ El novio de mi hermana es suizo y siempre dice que
ese lugar del que él proviene es un pueblo lleno de magia.
Nunca he viajado a Suecia, pues no tengo tanto dinero para ir.
Mejor hablaremos después cuando estés más tranquila. """

amount_of_diphtongs = 0
found_diphtongs = []
arr_words = Sentence.split()
for word in arr_words:
    for d in diphthongs:
        if d in word:
            amount_of_diphtongs += 1
            found_diphtongs.append(f"{word} - {d.upper()}")


print(f"We've found {amount_of_diphtongs} Diphtongs in this Phrase.")
response  = input("would you like to visualize the diphtongs we have found? y/n")
if(response.lower()=="y"):
    print(found_diphtongs)
else:
    print("Bye for now, fellows!")
