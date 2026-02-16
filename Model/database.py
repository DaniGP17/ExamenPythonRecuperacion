import os.path
import sqlite3

DB_PATH = "biblioteca.db"
SQL_PATH = "Data/crear_bd_biblioteca.sql"

def initialize_db(conn: sqlite3.Connection) -> None:
    with open(SQL_PATH, 'r') as file:
        queries = file.read().split(';')
        for query in queries:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

def get_connection() -> sqlite3.Connection:
    exists = os.path.exists(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    if not exists:
        initialize_db(conn)
    return conn