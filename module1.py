#module.py
#1번

from tkinter import *

class T:
    def __init__(self):
        self.window=Tk()
        self.label=Label(self.window,text="Hi!") 
        self.button=Button(self.window,text="click me",command=self.clicked)  
    def play(self):
        self.label.pack(side=LEFT)
        self.button.pack(side=LEFT)    
        self.window.mainloop() 
    def clicked(self):
        self.label['text']="cliked"
