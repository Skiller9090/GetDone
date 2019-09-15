from Account import *

accounts = {}

def base_account_create():
  global accounts
  new_account = Base_Account()
  new_account_num = new_account.get_all_info()[0]
  to_add = {new_account_num:new_account}
  accounts.update(to_add)
while command != "exit":
  command = (input("> ")+" ")
  command_base_with_args = command.split(" ")
  if command_base_with_args[0].lower() == "create":
    if command_base_with_args[1].lower == "base_account":
      CreateAccount.base_account_create()
  elif command_base_with_args[0] == "get_info":
    account_obj = accounts[command_base_with_args[1]]
    info = account_obj.get_all_info()
    for i in info:
      print(i)
  elif command_base_with_args[0] == "list_accounts":
    for i in accounts:
      print(i)
  else:
    print("Not A Command")
