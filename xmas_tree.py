# Build a Christmas Tree with the languages I have used for coding
# Made with ❤️ in Python 3 by Alvison Hunter - December 23rd, 2020
# Merry Xmas y'all from the Hunters. Jinotepe, Carazo, Nicaragua.
# Website: https://alvisonhunter.com/
languages = "delphi*foxpro*vba*csharp*javascript*python*typescript*"
def display_tree():
    global languages
    for elem in range(0,len(languages)):
        if (elem % 2) != 0:
            print(languages[0:elem].center(len(languages),' '))
    # Lets paint the trunk of the tree now using an inline sentence
    [print('********'.center(len(languages),' ')) for i in range(10)]

# Let us call the function now and draw the tree on the screen!
display_tree()


