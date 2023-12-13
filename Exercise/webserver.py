from flask import Flask, request, jsonify
from models import Students

app = Flask(__name__)

@app.route("/insert/<name>", methods=["GET"])
def add_student(name):
    new = Students(name, None)
    new.insert()
    return jsonify({"Success": True})




if __name__ == "__main__":
    app.run()