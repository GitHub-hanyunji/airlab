#module.py
#12번

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
                                        self.x+self.width,self.y+self.height,fill='red')
        # 버튼 배치할 프레임
        self.f=Frame(self.window)
    # 버튼을 누르면 실행
    # 사각형 움직이는 함수
    def move(self,key):
        # 왼쪽 키를 눌렀을 때
        if(key==1):
            if(self.x>=10):
                self.x-=10  # 왼쪽으로 이동
        # 오른쪽 키를 눌렀을 때
        elif(key==2):
            if(self.x+self.width)<=490:
                self.x+=10  # 오른쪽으로 이동
        # up 키를 눌렀을 때
        elif(key==3):
            if(self.y>=10):
                self.y-=10  # 위쪽으로 이동
        # down 키를 눌렀을 때
        else:
            if(self.y+self.height)<=340:
                self.y+=10  # 아래쪽을 이동
        # 사각형의 새로운 위치 업데이트
        self.w.coords(self.rect,self.x, self.y,self.x+self.width,self.y+self.height)
    def play(self):
        self.w.pack()
        # 왼쪽 버튼
        left=Button(self.f,text="<-(left)",command=lambda:self.move(1)).grid(row=0,column=2)
        # 오른쪽 버튼
        right=Button(self.f,text="->(right)",command=lambda:self.move(2)).grid(row=0,column=4)
        # up 버튼
        up=Button(self.f,text="^(up)",command=lambda:self.move(3)).grid(row=0,column=6)
        #down 버튼
        down=Button(self.f,text="v(down)",command=lambda:self.move(4)).grid(row=0,column=8)
        self.f.pack()
        self.window.mainloop()