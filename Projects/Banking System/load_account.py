# loading system to be added from account
from Account import *

def loadBAccount(num, cards, bal):
    newBAccount = Base_Account()
    newBAccount.load(num, cards, bal)
    return newBAccount

def loadDAccount(num, cards, bal, loans):
    newDAccount = Debit_Account()
    newDAccount.load(num, cards, bal, loans)
    return newDAccount
