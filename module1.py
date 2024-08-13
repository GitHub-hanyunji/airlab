#module.py
#1번

from tkinter import *
player="Xy"
list1=[]
def checked(i):
    global player
    global list1
    button=list1[i]
    
    if button["text"].strip():
        return
    button["text"]="     "+player+"      "
    if player=="X":
        player="O"
        button["bg"]="yellow"
    else:
        player="X"
        button["bg"]="lightgreen"
        
    
    
        
    
    
    
    