import time
import threading
import queue
import decimal
import math

"""
Hello I Made a cool pi calculatron thingy.
Made by Alex Gowers
Sorry for unreadable code :-)
"""
def calcpi(): # Where Pi is calculated and then sent to be printed every 100 iterations.
    global toprint
    decimal.getcontext().prec = 50
    doma = decimal.Decimal(2)
    domb = decimal.Decimal(3)
    domc = decimal.Decimal(4)
    summ = decimal.Decimal(0)
    num = decimal.Decimal(1)
    toprint = queue.Queue()
    while True:   
        for i in range(200):
            dom = decimal.Decimal(doma*domb*domc)
            fraction = decimal.Decimal(num/(dom))
            summ = decimal.Decimal(summ + fraction)
            doma = doma + 2
            domb = domb + 2
            domc = domc + 2
            num = num * -1
        toprint.put(3+decimal.Decimal(4*summ))

def clear(): # This is used to get 50:"\n" in a string
    clearlist = []
    for i in range(50):
        clearlist.append("\n")
    clearlist = "".join(clearlist)
    return clearlist
clear = clear() 

secthread = threading.Thread(target=calcpi) #Starts The Calc Thread
secthread.setDaemon(True)
secthread.start()
while True:#This Part Prints To Shell
    toprintready = []
    for i in range(50):
        for i in range(100):
            add = str(toprint.get()) 
        toprintready.append(add)
    add = str("In Queue---- ")+str(toprint.qsize())+ " ------"
    toprintready.append(add)
    qwerty = "\n".join(toprintready)
    print(clear+qwerty)
    del toprintready
    
    
    
        



