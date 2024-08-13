#main.py
#4번

from module4 import Rectangle

def main():
    r1=Rectangle(0,0,100,100)
    r2=Rectangle(10,10,100,100)
    if(r1.overlap(r2)):
        print("r1과 r2는 서로 겹칩니다")
    else:
        print("r1과 r2는 서로 겹치지 않습니다")
    
if __name__ == "__main__":
    main()  