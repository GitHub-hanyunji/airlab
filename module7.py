#module.py
#7번
from tkinter import *

class T:
    #생성자
    def __init__(self):
        self.window=Tk()
        self.entry=Entry(self.window,width=20)
        self.result_label=Label(self.window)
    # 변환버튼이 눌리면 실행되는 메서드
    def change(self):
        # 입력필드에서 값 가져와 정수로 변환
        inch_val=int(self.entry.get())
        # 인치를 cm로 변환
        result=inch_val*2.54
        # 결과 label에 변환된 값 문자열로 설정
        self.result_label['text']=str(result)
    def play(self):
        input_label=Label(self.window,text="인자를 입력하시오:").grid(row=0,column=0)
        self.entry.grid(row=0,column=1)
        result=Label(self.window,text="변환결과:").grid(row=1,column=0)
        self.result_label.grid(row=1,column=1)
        button=Button(self.window,text="변환!",command=self.change).grid(row=2,column=1)
        self.window.mainloop()
        