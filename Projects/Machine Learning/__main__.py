import math
import matplotlib
import random

class co:
    one = 0
    two = 0
test = range(1,102)
def calc(one=random.randint(1,401)):
    price = co.one + (co.two * one)
    return price,one

def cochange(change="add"):
    if change == "take":
        co.one -= int((100*price_check))+1
        co.two -= int((100*price_check))+1
    else:
        co.one += int((100*price_check))+1
        co.two += int((100*price_check))+1
def close(price,real):
    global price_check
    price_check = price/real
    if price_check < 1:
        cochange("a")
        a = "add"
    elif price_check == 1:
        t = "c"
        for i in test:
            a,o = calc(i)
            pc = a/(i*1000)
            print(pc)
            if pc == 1:
                None
            else:
                t = "f"
                
        if t == "f":
            t = "f"
            if pc < 1:
                cochange("a")
                a = "add"
            else:
                cochange("take")
                a = "took"
        print(t)
        if t == "c":
            a = "done"
    else:
        cochange("take")
        a = "took"
    return a

while True:
    price,ba = calc()
    out = close(price,(ba*1000))
    print(out,": ("+str(co.one)+","+str(co.two)+")")
    if out == "done":
        print("co one: "+str(co.one))
        print("co two: "+str(co.two))
        break
    
        
