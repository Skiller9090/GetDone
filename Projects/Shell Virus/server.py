import socket
from threading import *

url = ""

host = ""
port = 5883
activate = False
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))
server.listen(2)

cli, addr = server.accept()

def command_line():
    global url
    global activate

    while True:
        try:
            command = input("> ")
            command = command.split(" ")
            command[0] = command[0].lower()

            if command[0] == "url":
                url = command[1]
                print("[*] URL set to "+url)

            elif command[0] == "activate":
                if command[1].lower() == "true":
                    activate == True
                    print("[*] Activate set to True")
                else:
                    activate == False
                    print("[*] Activate set to False")
            else:
                print("[-] Invalid Command")
        except Exception as e:
            print("[-] Error")
command_line_thread = Thread(target=command_line)
command_line_thread.setDaemon(True)
command_line_thread.start()
while True:
    lis = cli.recv(4096).decode("utf-8")

    if "update" in lis and activate:
        cli.send(str("link: " + url).encode("utf-8"))
    else:
        cli.send("nothing".encode("utf-8"))
