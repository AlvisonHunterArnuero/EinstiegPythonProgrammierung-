# INTRODUCTION TO BASIC DECORATORS USING PYTHON 3
# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions
# that you don't want to modify. Let's take a look at this example:
# Made with ❤️ in Python 3 by Alvison Hunter - June 15th, 2021
# Website: https://alvisonhunter.com/

def my_decorator(func, caption):
    LINE = "━"
    TOP_LEFT = "┏"
    TOP_RIGHT = "┓"
    BOTTOM_LEFT = "┗"
    BOTTOM_RIGHT = "┛"

# This will be the wrapper for the function passed as params [func]
# Additionally, We will use the caption param to feed the text on the box
    def box():
        print(f"{TOP_LEFT}{LINE*(len(caption)+2)}{TOP_RIGHT}")
        func(caption)
        print(f"{BOTTOM_LEFT}{LINE*(len(caption)+2)}{BOTTOM_RIGHT}")
    return box

# This is the function that we will pass to  the decorator
# This will receive a param msg containing the text for the box


def boxed_header(msg):
    vline = "┃"
    title = msg.center(len(msg)+2, ' ')
    print(f"{vline}{title}{vline}")


decorated = my_decorator(boxed_header, "I bloody love Python")
decorated()
