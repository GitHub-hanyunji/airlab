#module.py
#4번

#Rectangle 클래스 정의
class Rectangle:
    #생성자
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
    #현재 사각형과 전달된 사각형이 겹치는지 확인하는 함수
    def overlap(self,r2):
        # 겹치면 True 반환
        if(self.x<=r2.x<=self.x+self.width and
        self.y<=r2.y<=self.y+self.height ):
            return True
        # 겹치지 않으면 False 반환
        else: return False
            