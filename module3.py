#module.py
#3번

#Box 클래스 정의
class Box:
    #생성자
    def __init__(self,l,h,d):
        self.length=l
        self.height=h
        self.depth=d
    # 상자의 정보 문자열로 변환하는 함수
    def __str__(self):
        return f"({self.length},{self.height},{self.depth})"
    # 상자의 가로 길이 반환
    def getLength(self):
        return self.length
    # 상자의 세로 길이 반환
    def getHeight(self):
        return self.height
    # 상자의 높이 길이 반환
    def getDepth(self):
        return self.depth
