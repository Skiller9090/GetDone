from merge_account import *
from Account import *

#0 = ID, 1 = Account_number, 2 = card_number, 3 = account balance

def check_balance(account_number):
    acc_data = getData(account_number)
    bal = acc_data[3]
    return bal
    