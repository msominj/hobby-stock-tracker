import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "hobby_stock_tracker.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            photo_path TEXT,
            needed BOOLEAN NOT NULL DEFAULT 0
        )
        ''')
        conn.commit()
