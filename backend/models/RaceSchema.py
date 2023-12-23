import sqlite3

def create_schema():
    conn = sqlite3.connect('backend/database/formula1.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS races (
                   
                   )''')