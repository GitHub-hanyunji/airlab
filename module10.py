#module.py
#10번

from tkinter import *
from typing import Any

class T:
    # 생성자
    def __init__(self):
        self.window=Tk()
        self.w=Canvas(self.window,width=500,height=500)
        self.width=200
        self.height=200
        self.rect=None
    # 사각형 크기 감소 함수
    # 마우스 왼쪽 키 누르면 실행되는 메서드
    def Decrease(self,event):
        # 사각형 최소 크기 제한
        if(self.width>=60 and self.height>=60):
            self.width-=10
            self.height-=10
        # 사각형 업데이트
        self.update_rectangle()
    # 사각형 크기 증가 함수
    # 마우스 오른쪽 키 누르면 실행되는 메서드
    def Increase(self,event):
        self.width+=10
        self.height+=10
        self.update_rectangle()
    # 사각형 업데이트 하는 메서드
    def update_rectangle(self):
        # 이전에 그려진 사각형이 있으면 삭제
        if self.rect is not None:
            self.w.delete(self.rect)  
        self.rect = self.w.create_rectangle(50, 50, self.width, self.height) 
    def play(self):
        self.window.geometry("500x500")
        self.w.pack()
        self.update_rectangle()
        # 마우스 왼쪽 버튼 클릭시
        self.window.bind("<Button-1>",self.Decrease)
        # 마우스 오른쪽 버튼 클릭시
        self.window.bind("<Button-3>",self.Increase)
        self.window.mainloop()