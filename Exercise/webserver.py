from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/insert/<name>", methods=["GET"])
def add_student(name):
    with sqlite3.connect("example.db") as conn:
        cursor = conn.cursor()
        sql = """INSERT INTO students (name) VALUES {?}"""
        cursor.execute(sql, (name,))
    return jsonify({"Success": True})



if __name__ == "__main__":
    app.run()