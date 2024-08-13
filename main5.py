#main.py
#5번

from module5 import Triangle

def main():
    triangle=Triangle(90,30,60)
    print(triangle.checkAngles())
    
if __name__ == "__main__":
    main()