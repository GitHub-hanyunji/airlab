#module.py
#5번
from tkinter import *

class T:
    #생성자
    def __init__(self):
        self.window=Tk()
        self.label=Label(self.window,text="0")
        self.count=0
    def clicked(self,key):
        # 증가 버튼이면
        if(key):
            # count 1씩 증가
            self.count+=1
        # 감소 버튼이면
        else:
            # count 1씩 감소
            self.count-=1
        # 라벨에 바뀐 count 값 넣기
        self.label['text']=str(self.count)
    def play(self):
        # 감소 버튼, click 함수에 key=False 전달
        button1=Button(self.window,text="감소",command=lambda:self.clicked(False))
        button1.pack(side=LEFT)
        self.label.pack(side=LEFT)
        # 증가 버튼, click 함수에 key=True 전달
        button2=Button(self.window,text="증가",command=lambda:self.clicked(True))
        button2.pack(side=LEFT)
        self.window.mainloop()
        