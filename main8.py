#main.py
#8번

from module8 import printSong

def main():
    aSong=printSong(["TWINKLE, twinkle, little star",
                    "How I wonder what you are!",
                    "Up above the world so high",
                    "Like a diamond in the sky."])
    aSong.sing()
    
if __name__ == "__main__":
    main()