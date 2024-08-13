#module.py
#7번

# PhoneBook 클래스 정의
class PhoneBook:
    #생성자
    def __init__(self):
        self.contacts={}
        self.dic_count=0
    # 연락처 정보를 문자열로 변환하는 함수
    def __str__(self):
        list1=[]
        for x in self.contacts.values():
            # 값이 있으면 list에 추가, 없으면 빈문자열 추가
            list1.append(x.get('name')) if x.get('name') is not None else ' '
            list1.append(f"moblie phone:\t{x.get('moblie')}") if x.get('moblie') is not None else ' '
            list1.append(f"office phone:\t{x.get('office')}") if x.get('office') is not None else ' '
            list1.append(f"email address:\t{x.get('email')}") if x.get('email') is not None else ' '
            # 줄바꿈
            list1.append('\n')
        # 리스트를 줄바꿈으로 결합하여 반환
        return '\n'.join(list1)
    # 한 사람의 연락처를 추가하는 함수
    def add(self,name,mobile=None,office=None,email=None):
        # 연락처 정보 딕셔너리에 저장
        self.contacts[self.dic_count]={
            "name":name,
            "moblie":mobile,
            "office":office,
            "email":email
        }
        self.dic_count+=1