# ---------------------------------------------------------------------------
# Let's built a multi-colored lines Spirograph using python and turtle module
# Made with ❤️ in Python 3 by Alvison Hunter - March 23th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------

import turtle as tt

tt.setup(800,800)
tt.pensize(2)
tt.speed(0)
wn = tt.Screen() 
wn.title("Build a SpiroGraph!") 
wn.bgcolor("black")

for i in range(12):
    for c in ['red','magenta','blue','cyan','green','white','yellow']:
        tt.color(c)
        tt.circle(120)
        tt.left(15)
    tt.hideturtle()
wn.mainloop()

