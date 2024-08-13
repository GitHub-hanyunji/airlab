#main.py
#1번

from module1 import *


def main():
    global list1
    window=Tk()
    window.geometry("500x500")
    for i in range(10):
        b=Button(window,text="       ",command=lambda k=i: checked(k),width=10, height=5)
        b.grid(row=i//3,column=i%3)
        list1.append(b)
    window.mainloop()
    
if __name__ == "__main__":
    main()