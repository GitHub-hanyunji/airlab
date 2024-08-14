#module.py
# 6번
from tkinter import *
import random

class T:
    #생성자
    def __init__(self):
        self.window=Tk()
        # 버튼 누르면 랜덤 숫자 생성해 label 작성
        self.button=Button(self.window,text="굴리기",command=self.random_int)
        self.lable=Label(self.window,width=5)
    def random_int(self):
        # 1부터 6사이 랜덤 숫자
        rand=random.randint(1,6)
        self.lable['text']=str(rand)
    def play(self):
        self.lable.grid(row=0,column=0)
        self.button.grid(row=0,column=1)
        self.window.mainloop()