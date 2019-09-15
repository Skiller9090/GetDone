from tkinter import *
from threading import *
class debug():
    def start():
        global root,betvar,nextcard
        root = Tk()
        betvar = StringVar()
        betvar.set("0")
        label = Label(root,textvariable=betvar)
        label.pack()
        nextcard =  StringVar()
        nextcard.set("NULL")
        label = Label(root,textvariable=nextcard)
        label.pack()
        root.mainloop() 
    def endless_interchange():
        global bet,deck
        while True:
            try:
                betvar.set(bet)
                nextcard.set(deck[0]+","+deck[1]+","+deck[2])
            except:
                None
    def update(var):
        globals().update(var)
ei = Thread(target=debug.endless_interchange)
ei.setDaemon(True)
ei.start()
gui = Thread(target=debug.start)
gui.setDaemon(True)
gui.start()
