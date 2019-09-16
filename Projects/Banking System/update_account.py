from sql import *
from Account import *
from load_account import *
from merge_account import *

# getDataU = getData()

# def getDataU(*args):
#     accountDetails = []
#     for acc_number in args:
#         account_no = get_details(acc_number)
#         accountDetails.append(account_no)
#     return accountDetails

def UpdateAccount(*args):
    account_details = getData(args)
    for account_no in account_details:
        acc_num = account_no[1]
        acc_cards = account_no[2]
        acc_bal = account_no[3]
    return acc_num, acc_cards, acc_bal
    