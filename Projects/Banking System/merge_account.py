from Account import *
from load_account import *
from sql import *
# *args passes it into a list

def getData(*args):
    accounts = []
    for acc_number in args:
        account = get_details(acc_number)
        accounts.append(account)
    return accounts
#0 = ID, 1 = Account_number, 2 = card_number, 3=account balance
def mergeAccount(*args):
    account_details = getData(args)
    bal = 0
    for account in account_details:
        bal += account[3] 

    newAccount = Base_Account()
    account_num, account_cards, account_bal = newAccount.get_all_info()
    account_bal = bal
    newAccount.load(account_num, account_cards, account_bal)
    conn,cursor = create_connection("./accounts.db")
    create_table(conn,cursor)
    save_account(conn,cursor,account_num, account_cards, account_bal)
    for account in account_details:
        delete_account(conn,cursor,account)
    conn.close()
    # use main account number (main account to be merged into)
    # + the $ in the accounts
    # TO DELETE: account that is merged from
    return account_num

    # push mergedAccount into db, not sure how to do that again