from merge_account import *

def UpdateAccount(*args):
    account_details = getData(args)
    for account_no in account_details:
        acc_num = account_no[1]
        acc_cards = account_no[2]
        acc_bal = account_no[3]
    return acc_num, acc_cards, acc_bal
    
