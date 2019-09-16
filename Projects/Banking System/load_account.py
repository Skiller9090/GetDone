# loading system to be added from account
from Account import *
from sql import *

def loadBAccount(num, cards, bal):
    newBAccount = Base_Account()
    newBAccount.load(num, cards, bal)
    return newBAccount

def loadDAccount(num, cards, bal, loans):
    newDAccount = Debit_Account()
    newDAccount.load(num, cards, bal, loans)
    return newDAccount

def get_details(account_number):
    conn, cursor = create_connection("./accounts.db") 
    data = get_account(conn, cursor, account_number)