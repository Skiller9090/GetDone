from create_account import *

accounts = {}
command = ""

while command != "exit":
    command = (input("> ")+" ")
    command_base_with_args = command.split(" ")
    if command_base_with_args[0].lower() == "create":
        if command_base_with_args[1].lower() == "base_account":
            to_add = base_account_create()
            accounts.update(to_add)
    elif command_base_with_args[0] == "get_info":
        account_obj = accounts[int(command_base_with_args[1])]
        info = account_obj.get_all_info()
        acc_num = info[0]
        cards = info[1]
        bal = info[2]
        print("Account Number:",end=" ")
        print(acc_num)
        print("Account Cards:",end=" ")
        print(cards)
        print("Account Balance: £",end="")
        print(bal)
    elif command_base_with_args[0] == "list_accounts":
        for i in accounts:
            print(i)
    else:
        print("Not A Command")
