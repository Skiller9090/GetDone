import sqlite3
from sqlite3 import Error
 

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn ,conn.cursor()

def create_table(conn,cursor):
    command = """CREATE TABLE IF NOT EXISTS accounts (
    id integer PRIMARY KEY,
    account_number integer,
    account_cards text NOT NULL,
    account_balance integer
);"""
    cursor.execute(command)

def save_account(conn,cursor,acc_num,acc_cards,acc_bal):
    sql = '''INSERT INTO accounts(account_number,account_cards,account_balance)
    VALUES(?,?,?)
'''
    acc_cards = "|".join(acc_cards)
    cursor.execute(sql,(acc_num,acc_cards,acc_bal))
    conn.commit()
    return cursor.lastrowid

def get_all_accounts(conn,cursor):
    cursor.execute("SELECT * FROM accounts")
    rows = cur.fetchall()
    return rows
def get_account(conn,cursor,account_number)
    cursor.execute("SELECT * FROM accounts WHERE account_number = "+str(account_number))
    rows = cur.fetchall()
    return rows
def update_account(conn,cursor,acc_num,acc_cards,acc_bal):
    sql = """UPDATE accounts
SET account_number =?
    account_cards = ?
    account_balance = ?
WHERE account_number = ?"""
    acc_cards = "|".join(acc_cards)
    cursor.execute(sql,(acc_num,acc_cards,acc_bal,acc_num))
    conn.commit()
