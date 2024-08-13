#main.py
#2번

from module2 import Rocket

def main():
    myRocket=Rocket()
    print("로켓의 높이:",myRocket.y)
    myRocket.moveUp()
    print("로켓의 높이:",myRocket.y)

if __name__ == "__main__":
    main()