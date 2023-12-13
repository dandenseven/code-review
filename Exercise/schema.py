import sqlite3

def schema():
    with sqlite3.connect("examlpe.db") as conn:
        cursor = conn.cursor()
        sql = """CREATE TABLE students(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR
        )"""
        cursor.execute(sql)


if __name__ == "__main__":
    schema()


