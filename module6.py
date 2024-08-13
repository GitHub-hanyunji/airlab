#module.py
# 6번

# Person 클래스 정의
class Person:
    #생성자
    def __init__(self,n,m=None,o=None,e=None):
        self.name=n
        self.mobile=m
        self.office=o
        self.email=e
    #Person의 정보를 문자열로 변환하는 함수
    def __str__(self):
        list1=[]
        list1.append(f"\"{self.name}\"") if self.name is not None else ' '
        list1.append(f"moblie=\"{self.mobile}\"") if self.mobile is not None else ' '
        list1.append(f"office=\"{self.office}\"") if self.office is not None else ' '
        list1.append(f"email=\"{self.email}\"") if self.email is not None else ' '
        result=', '.join(list1)
        return f"Person({result})"
    # Person의 이메일 정보 변환
    def setEmail(self,e):
        self.email=e
    # Person의 이메일 정보 반환
    def getEmail(self):
        return self.email