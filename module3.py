#module.py
#3번
from tkinter import *

class T:
    def __init__(self):
        self.window=Tk()
    def play(self):
        for i in range(3):
            for j in range(10):
                button=Button(self.window,text=f"{i}행,{j}열").grid(row=i,column=j)
        self.window.mainloop()        
