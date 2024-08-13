#module.py
#9번

import turtle
# Tur 클래스 정의
class Tur:
    #생성자
    def __init__(self,direction,sp):
        self.t=turtle.Turtle()
        self.t.shape(sp) # 거북이 모양
        self.direction=direction #거북이 방향
    def run(self):
        # 방향이 왼쪽일때
        if(self.direction=="left"):
            self.t.setheading(180)
            self.t.fd(100)
            self.t.right(90)
            self.t.fd(50)
            self.t.left(90)
            self.t.fd(100)
        # 방향이 오른쪽일때
        else:
            self.t.setheading(0)
            self.t.fd(100)
            self.t.right(90)
            self.t.fd(50)
            self.t.left(90)
            self.t.fd(100)
        