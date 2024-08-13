#module.py
#5번

# Triangle 클래스 정의
class Triangle:
    #생성자
    def __init__(self,a1,a2,a3):
        self.angle1=a1
        self.angle2=a2
        self.angle3=a3
        self.numberOfSides=3
    # 삼각형의 내각이 180도인지 확인하는 함수  
    def checkAngles(self):
        result=self.angle1+self.angle2+self.angle3
        if(result==180):
            return True
        else:
            return False