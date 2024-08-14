#module.py
#14번

from tkinter import *
import random

class T:
    # 생성자
    def __init__(self):
        self.window=Tk()
        self.w=Canvas(self.window,width=600,height=400,bg='white')
        self.color=["red","orange","yellow","green","blue","violet"]
        
    #위치, 크기, 색상 랜덤으로 사각형 그리기
    def random_rand(self):
        for i in range(10):
            x=random.randint(0,50)
            y=random.randint(0,50)
            width=random.randint(50,500)
            height=random.randint(50,350)
            random_color=random.choice(self.color)
            self.w.create_rectangle(x,y,x+width,y+height,fill=random_color)
    def play(self):
        self.w.pack()
        self.random_rand()
        self.window.mainloop()