#module.py
#11번

from tkinter import *

class T:
    # 생성자
    def __init__(self):
        self.window=Tk()
        self.w=Canvas(self.window,width=500,height=300)
        self.w.pack()
        self.x=100
        self.y=100
        self.speed=5
        self.text=self.w.create_text(self.x,self.y,text="파이썬 커피샵으로 오세요!")
    # 애니메이션 메서드
    def animation(self):
        # x 좌표를 이동속도만큼 증가
        self.x+=self.speed
        # 글자가 오른쪽을 넘어가려고 하면 왼쪽으로 이동
        if self.x>500:
            self.x=0
        # canvas에서 위치 업데이트
        self.w.coords(self.text,self.x,self.y)
        # 50ms 후에 anmation 메서드 다시 호출
        self.window.after(50,self.animation)
    def play(self):
        self.animation()
        self.window.mainloop()