import sqlite3

class Students:


    def __init__(self, name, pk):
        self.pk = pk
        self.name = name

    def insert(self):
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            sql = """INSERT INTO students (name) VALUES {?}"""
            cursor.execute(sql, {self.name,})
    
    def insert(self):
        with sqlite3.connect("example.db") as conn:
            cursor = conn.cursor()
            sql = """"""
            cursor.execute(sql)