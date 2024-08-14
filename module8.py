#module.py
#8번
from tkinter import *

# printSong 클래스 정의
class T:
    def __init__(self):
        self.window=Tk()
        self.entry_id=Entry(self.window,width=20)
        self.entry_password=Entry(self.window,width=20)
        self.result=Label(self.window,width=10)
    # 로그인 버튼이 눌렸을 때 실행되는 메서드
    def login(self):
        Id=self.entry_id.get()
        password=self.entry_password.get()
        if(Id=="abcdef" and password=="123456"):
            self.result['text']="로그인 성공"
        else:
            self.result['text']="로그인 실패"
    # 취소 버튼이 눌렸을 때 실행되는 메서드
    def cancel(self):
        # 입력 필드 초기화 (ID와 비밀번호를 삭제)
        self.entry_id.delete(0, END)
        self.entry_password.delete(0, END)
        self.result['text'] = ""  # 결과 레이블 초기화
    def play(self):
        self.window.geometry("200x70")
        label1=Label(self.window,text="아이디").grid(row=0,column=0,sticky='e')
        label2=Label(self.window,text="패스워드").grid(row=1,column=0,sticky='e')
        self.entry_id.grid(row=0,column=1)
        self.entry_password.grid(row=1,column=1)
        login_button=Button(self.window,text="로그인",command=self.login).place(x=7,y=43)
        cancel_button=Button(self.window,text="취소",command=self.cancel).place(x=60,y=43)
        self.result.place(x=110,y=43)
        self.window.mainloop()
    