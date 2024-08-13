#main.py
#9번

import module9
from module9 import Tur

def main():
    lee=Tur("left","circle")
    lee2=Tur("right","turtle")
    lee.run()
    lee2.run()
    module9.turtle.mainloop()
    module9.turtle.bye()
if __name__ == "__main__":
    main()