#module.py
#8번

# printSong 클래스 정의
class printSong:
    #생성자
    def __init__(self,song):
        self.song=song
    def sing(self):
        result='\n'.join(self.song)
        print(result)
    