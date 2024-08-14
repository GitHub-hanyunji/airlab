#module.py
#2번

from tkinter import *
#Rocket 클래스 정의
class T:
    def __init__(self):
        self.window=Tk()
        # label: 배경색=오렌지, 글자색=파랑
        self.label=Label(self.window,text="Hello, I'm Label",fg='blue',bg='orange',width=50,height=3)
    def play(self):
        self.label.pack()
        self.window.mainloop()