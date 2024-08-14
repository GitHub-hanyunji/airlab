#module.py
#9번

from tkinter import *

class T:
    #생성자
    def __init__(self):
        self.window=Tk()
    def play(self):
        name_label=Label(self.window,text="이름").grid(row=0,column=0,columnspan=2)
        job_label=Label(self.window,text="직업").grid(row=1,column=0,columnspan=2)
        nation_label=Label(self.window,text="국적").grid(row=2,column=0,columnspan=2)
        for i in range(3):
            entry=Entry(self.window,width=20)
            entry.grid(row=i,column=3)
        show_button=Button(self.window,text="Show").grid(row=3,column=0)
        quit_button=Button(self.window,text="quit").grid(row=3,column=1)
        self.window.mainloop()