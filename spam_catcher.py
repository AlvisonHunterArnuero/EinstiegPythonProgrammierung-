# let us create a list containing a set of phrases that could be considered as spam.
# Made with ❤️ in Python 3 by Alvison Hunter - January 28th, 2021
spams_lst = ["make","money","buy","subscribe","click","claim","prize","win","lottery"]
def spam_catcher():
  # Bool variable to determine if the phrase is an spam or not
  is_spam = False
  try:
    # let us ask for the phrase y convert it to lowercase
    phrase = input("Enter some phrase: \n").lower()
    for el in spams_lst:
      if el in phrase:
        is_spam = True
        break
      else:
        continue
  except:
    print("Uh oh, an error has occurred. Program terminated")
    quit()
  else:
    print("This is Spam") if is_spam else print("This is not Spam")
    print("Thank you for using the Spam Catcher - January 2021")

spam_catcher()
