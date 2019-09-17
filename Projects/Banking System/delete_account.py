from sql import *

def DeleteAccounts(account_number):
    conn, cursor = create_connection('./accounts.db')
    for acc in account_number:
        delete_account(conn, cursor, acc)
    conn.close()