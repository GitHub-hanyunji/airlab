#module.py
#4번
from tkinter import *
#Rectangle 클래스 정의
class T:
    #생성자
    def __init__(self):
        self.window=Tk()
    def play(self):
        self.window.geometry("270x150")
        # sticky='e' 오른쪽으로 정렬
        label1=Label(self.window,text="이름:").grid(row=0,column=2,sticky='e')
        label2=Label(self.window,text="주소:").grid(row=1,column=2,sticky='e')
        label3=Label(self.window,text="도:").grid(row=2,column=2,sticky='e')
        label4=Label(self.window,text="우편번호:").grid(row=3,column=2,sticky='e')
        label5=Label(self.window,text="국가:") .grid(row=4,column=2,sticky='e') 
        entry1=Entry(self.window,width=30).grid(row=0,column=3,columnspan=2)
        entry2=Entry(self.window,width=30).grid(row=1,column=3,columnspan=2)
        entry3=Entry(self.window,width=30).grid(row=2,column=3,columnspan=2)
        entry4=Entry(self.window,width=30).grid(row=3,column=3,columnspan=2)
        entry5=Entry(self.window,width=30) .grid(row=4,column=3,columnspan=2)
        button1=Button(self.window,text="Clear").place(x=160,y=110)
        button2=Button(self.window,text="Submit").place(x=210,y=110)
        self.window.mainloop()