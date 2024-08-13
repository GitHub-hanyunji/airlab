#module.py
#2번

#Rocket 클래스 정의
class Rocket:
    # 생성자
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    #로켓의 y좌표가 1만큼 증가
    def moveUp(self):
        self.y+=1