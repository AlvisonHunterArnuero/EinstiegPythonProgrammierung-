from tkinter import *
root = Tk()
root.title('Logon Screen')
Label(root, text='Click at different\n locations in the frame below').pack()
def mycallback(event):
 print(dir(event))
 print("you clicked at", event.x, event.y)
myframe = Frame(root, bg='khaki', width=130, height=80)
myframe.bind("<Button-1>", mycallback)
myframe.pack()
root.mainloop()

