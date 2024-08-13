#main.py
#3번

from module3 import Box

def main():
    b1=Box(100,100,100)
    print(b1)
    print("상자의 부피는",b1.getHeight()*b1.getLength()*b1.getDepth()) 

if __name__ == "__main__":
    main() 