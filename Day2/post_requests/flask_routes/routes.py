# POST Requests

"""
POST /data HTTP/1.1
Content-Type: application/x-www-from-urlencoded
Content-Type: application/json
Content-Length: 30

Key1=thefirstvalue&key2=other
{key1: "thefirstvalue"}, key2: "other"}

"""


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test", methods=["POST"])
def get_data():
    data = request.get_data()
    data2 = request.get_json() 
    # requires Content_Type to be application/json
    if data2:
        first = data2.get("key1")
    print(data, data2)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run()
