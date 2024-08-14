#module.py
#13번

from tkinter import *

class T:
    # 생성자
    def __init__(self):
        self.window=Tk()
        self.w=Canvas(self.window,width=500,height=350,bg='white')
        self.x=200
        self.y=150
        self.width=100
        self.height=100
        # 사각형 캔버스에 그리기
        self.rect=self.w.create_rectangle(self.x,self.y,
                                        self.x+self.width,self.y+self.height,fill='green')
    def update(self):
        self.w.coords(self.rect,self.x, self.y,self.x+self.width,self.y+self.height)
    # 사각형 움직이는 함수
    # 왼쪽 키를 눌렀을 때
    def move_left(self,event):
        if(self.x>=10):
            self.x-=10  # 왼쪽으로 이동
        self.update()
    # 오른쪽 키를 눌렀을 때
    def move_right(self,event):
        if(self.x+self.width)<=490:
            self.x+=10  # 오른쪽으로 이동
        self.update()
    # up 키를 눌렀을 때        
    def move_up(self,event):
        if(self.y>=10):
            self.y-=10  # 위쪽으로 이동
        self.update()
    # down 키를 눌렀을 때
    def move_down(self,event):
        if(self.y+self.height)<=340:
            self.y+=10  # 아래쪽을 이동
        self.update()
    def play(self):
        self.w.pack()
        # 이벤트
        self.window.bind("<Left>",self.move_left)
        self.window.bind("<Right>",self.move_right)
        self.window.bind("<Up>",self.move_up)
        self.window.bind("<Down>",self.move_down)
        
        self.window.mainloop()