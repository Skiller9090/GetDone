from sql import *

def get_all_info(account_num):
    conn,cursor = create_connection("./accounts.db")
    info = get_account(conn,cursor,account_num)
    conn.close()
    return info
