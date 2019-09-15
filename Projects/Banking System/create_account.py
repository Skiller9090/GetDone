from Account import *
from sql import *

def base_account_create():
    global accounts
    new_account = Base_Account()
    acc_num,acc_cards,acc_bal = new_account.get_all_info()
    conn,cursor = create_connection("./accounts.db")
    create_table(conn,cursor)
    save_account(conn,cursor,acc_num,acc_cards,acc_bal)
    conn.close()
    return acc_num

