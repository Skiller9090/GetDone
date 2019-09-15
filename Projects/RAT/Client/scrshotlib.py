import mss
import time

def tss(name=''):
    if name == '':
        t=time.gmtime()
        name = "SS "+str(t.tm_hour)+"."+str(t.tm_min)+"."+str(t.tm_sec)+" "+str(t.tm_mday)+"-"+str(t.tm_mon)+"-"+str(t.tm_year)
    obj = mss.mss()
    with obj as m:
        m.shot(output=(name+".png"))
    return name+'.png'
