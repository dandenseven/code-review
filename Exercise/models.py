import sqlite3

class Students:


    def __init__(self, name, pk):
        self.pk = pk
        self.name = name

    def insert(self):
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO students (name) VALUES {?}"""
            cursor.execute(sql, (self.name,))
    
    @classmethod
    def select_all(cls):
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM students;"""
            cursor.execute(sql)
