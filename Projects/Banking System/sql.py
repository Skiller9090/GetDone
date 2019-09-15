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

