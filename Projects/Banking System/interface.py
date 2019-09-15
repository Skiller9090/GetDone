from create_account import *
from get_info import *
accounts = {}
command = ""

while True:
    command = (input("> ")+" ")
    command_base_with_args = command.split(" ")
    if command_base_with_args[0].lower() == "create":
        if command_base_with_args[1].lower() == "base_account":
            to_add = base_account_create()
            accounts.update(to_add)
    elif command_base_with_args[0] == "get_info":
        account_obj = accounts[int(command_base_with_args[1])]
        acc_num,cards,bal = get_all_info(account_obj)
        print("Account Number:",end=" ")
        print(acc_num)
        print("Account Cards:",end=" ")
        print(cards)
        print("Account Balance: £",end="")
        print(bal)
    elif command_base_with_args[0] == "list_accounts":
        for i in accounts:
            print(i)
    elif command_base_with_args[0] == "exit":
        exit()
    else:
        print("Not A Command")
