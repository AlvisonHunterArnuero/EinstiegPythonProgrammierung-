# ---------------------------------------------------------------------------
# Let's built a multi-colored lines Spirograph using python and turtle module
# Made with ❤️ in Python 3 by Alvison Hunter - May 8th, 2022
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------
import turtle as tt
wn = tt.Screen() 
wn.title("Build a Avatar Logo!") 
wn.bgcolor("black")

tt.setup(800,800)
tt.pensize(1)
tt.speed(0)
tt.color('orange')
tt.hideturtle()
c_lst = ['red','magenta','blue','cyan','green','white','yellow']

n=1
i =0
p=True
while True:
    tt.circle(n)
    n=n-1 if p else n+1
    if n==0 or n==60:
        p = not p
        if i == 6:
            break
        else:
            tt.color(c_lst[i])
            i=i+1
       
    tt.left(1)
    tt.forward(3)
    
    
wn.mainloop()
