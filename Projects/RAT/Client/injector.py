import os

drive = os.getenv("SystemDrive")
username = os.getlogin()
directory = drive+"\\Users\\"+username+"\\AppData\\Local\\Google\\Extensions"
os.mkdir(directory)

