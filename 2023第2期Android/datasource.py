import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql_projects = """
    CREATE TABLE IF NOT EXISTS led(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		date TEXT NOT NULL,
		state INTEGER NOT NULL		
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_projects)
        print("Table created successfully")  
    except Error as e:
        print(e)

def insert_data(conn, state):
    sql_insert = """
    INSERT INTO led(date, state) VALUES(datetime('now'), ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql_insert, (state,))
    conn.commit()
    conn.close()

