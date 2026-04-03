import sqlite3

def get_user(username):
    conn = sqlite3.connect("app.db")
    # SQL INJECTION - this is actually vulnerable
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchone()

def delete_user(user_id):
    conn = sqlite3.connect("app.db")
    query = f"DELETE FROM users WHERE id = {user_id}"
    conn.execute(query)
    conn.commit()
