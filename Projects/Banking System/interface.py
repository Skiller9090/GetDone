from create_account import *
from get_info import *
accounts = {}
command = ""

while True:
    command = (input("> ")+" ")
    command_base_with_args = command.split(" ")
    if command_base_with_args[0].lower() == "create":
        if command_base_with_args[1].lower() == "base_account":
            number = base_account_create()
            print("[+] Created Account")
            print("[£] Account Number: "+str(number))
    elif command_base_with_args[0] == "get_info":
        account_num = int(command_base_with_args[1])
        info = get_all_info(account_num)
        print("SQL ID: {}\nAccount Number: {}\nCards: {}\nAccount Balance: {}".format(str(info[0][0]),str(info[0][1]),str(info[0][2])+" ",str(info[0][3])))
    elif command_base_with_args[0] == "list_accounts":
        conn, cursor = create_connection("./accounts.db")
        for i in get_all_accounts(conn,cursor):
            print("[*] Account Number: "+str(i[1]))
        conn.close()
    elif command_base_with_args[0] == "exit":
        exit()
    else:
        print("Not A Command")
