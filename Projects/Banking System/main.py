from Account import *
import CreateAccount

while command != "exit":
  command = input("> ")
  command_base_with_args = command.split(" ")
  if command_base_with_args[0].lower() == "create":
    if command_base_with_args[1].lower == "base_account":
      CreateAccount.base_account_create()
  elif command_base_with_args[0] == "get_info":
    None
    #gets all info on account
  else:
    print("Not A Command")
