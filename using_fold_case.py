# -------------------------------------------------------------------------
# Write a python program to find out whether a given post is talking about
# “Harry” or not. it can be in both uppercase an lowercase example:
# -HARry,HarRY,harry,HARRY,hArrY,Harry
# Made with ❤️ in Python 3 by Alvison Hunter - January 24th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# -------------------------------------------------------------------------
post = input("Enter post content: ")
print("Talks about Harry!" if "harry" in post.casefold() else "Doesn't Talk about Harry!")