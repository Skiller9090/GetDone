import socket
import time
import urllib.request

obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
time_per_signal = 5
addr = ("127.0.0.1",5883)

class handlers:
    def nothing():
        return "nothing"
    def activate(link):
        #Download and install
        return "nothing"
def connect_to(obj,addr):
    while True:
        try:
            obj.connect(addr)
            break
        except:
            time.sleep(3)
            continue
    check_loop(obj,addr)
def check_loop(obj,addr):
    while True:
        try:
            obj.send(b"update")
            data = obj.recv(4096).decode()
            if data == "nothing":
                done = handlers.nothing()
            elif "link: " in data:
                link = data[6:]
                handlers.activate(link)
            else:
                continue
            time.sleep(time_per_signal)
        except Exception as e:
            if "Broken pipe" in e:
                break
        connect_to(obj,addr)
connect_to(obj,addr)
