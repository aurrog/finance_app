import sqlite3
import datetime


def add_transaction(transaction_type, amount, description, date=None):
    if not date:
        date = datetime.date.today()

    conn = sqlite3.connect('db/finance.db')
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO transactions (type, amount, description, date)
            VALUES (?, ?, ?, ?)
        ''', (transaction_type, amount, description, date))
    conn.commit()
    conn.close()


def get_transaction_by_id(transaction_id):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions WHERE id = ?', (transaction_id,))
    transaction = cursor.fetchone()
    conn.close()
    return transaction


def get_transactions():
    conn = sqlite3.connect('db/finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    conn.close()
    return transactions


def update_transaction(transaction_type, amount, description, date, transaction_id):
    conn = sqlite3.connect('db/finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE transactions
        SET type = ?, amount = ?, description = ?, date = ?
        WHERE ID = 9
    ''', (transaction_type, amount, description, date, transaction_id))
    conn.commit()
    conn.close()


def delete_transaction(transaction_id):
    conn = sqlite3.connect('db/finance.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    conn.close()
