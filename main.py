import tkinter
import os
from PIL import ImageTk, Image
from speechsdk import StartConversation

#
#Actual window        
window = tkinter.Tk()
window.geometry('1000x1000')
window.title('Game')
window.configure(bg = 'Indian red')

#Pictures
path = 'CopenhacksLogo.png'
img = ImageTk.PhotoImage(Image.open(path))
panel = tkinter.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

# labels
lbl1 = tkinter.Label(window,text = "KIM SPEECH", font = ("Arial", 40))
lbl1.place(relx = .5, rely = .1, anchor='c')
lbl2 = tkinter.Label(window, text = "Anything you wanna talk about?")
lbl2.place(relx = .5, rely = .90, anchor='c')

#Buttons
# start = tkinter.Button(text = 'Hello', height = 5, width = 25, font =
# ('Helvetica', 12))
# start.place(relx = .5, rely = .25, anchor='c')

# function for button press action
def clicked():
    lbl2.configure(text = "I'm listening..")
    StartConversation()

# create first button
btn1 = tkinter.Button(window, text = "Yes!", command = clicked)
btn1.place(relx = .5, rely = .95, anchor='c')

# exitbutton = tkinter.Button(text = 'Exit Game', command = quit, height = 5, 
# width = 15, fg = 'red')
# exitbutton.place(relx = .5, rely = .85, anchor='c')

window.mainloop()
