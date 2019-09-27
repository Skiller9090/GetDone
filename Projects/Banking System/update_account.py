from sql import *

def UpdateAccounts(account_numbers, acc_cards, acc_bal):
    conn, cursor = create_connection('./accounts.db')
    for account_no in account_numbers:
        update_account(conn, cursor, account_no, acc_cards, acc_bal)
    conn.close()
