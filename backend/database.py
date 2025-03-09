import sqlite3

def init_database():
    conn = sqlite3.connect('db/finance.db')
    cursor = conn.cursor()


    query = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT not NULL, -- income/expense/wish
            amount REAL not NULL,
            description TEXT,
            date TEXT not NULL
        )
    """
    cursor.execute(query)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_database()