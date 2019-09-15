import time
import cv2

def takepic():
    try:
        c = cv2.VideoCapture(0)
        time.sleep(5)
        t=time.gmtime()
        name = "WS "+str(t.tm_hour)+"."+str(t.tm_min)+"."+str(t.tm_sec)+" "+str(t.tm_mday)+"-"+str(t.tm_mon)+"-"+str(t.tm_year)+".png"
        s, e = c.read()
        cv2.imwrite(name,e)
        return name
            
    except:
        None
