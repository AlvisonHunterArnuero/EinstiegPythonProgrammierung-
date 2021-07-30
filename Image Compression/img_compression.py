# ---------------------------------------------------------------------------------------------
# Python Tricks and tips for better coding - Python 3 - Basic Python coding
# Made with ❤️ in Python 3 by Alvison Hunter - May 3rd, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------
import PIL
from PIL import Image
from tkinter.filedialog import input

file_path = askopenfilename()
img-PIL.image.open(file_path)

myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path + "compressed.jpg")

