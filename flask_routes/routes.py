from flask import Flask, request, jsonify
from models.listing import Listing
# Client-side code would SEND a request
# This is server-side code. It's designed to RECEIVE requests

app = Flask(__name__)

@app.route("/test", methods= ["GET"])
def show_status():
    return jsonify({"status": "running"})


@app.route("/string/<input_string>", methods=["GET"])
def reverse_string(input_string):
    return jsonify({"reversed": input_string[::-1],
                    "original": input_string})
    


@app.route("/list/all_items", methods=["GET"])
def all_items():
    # needs no input (we want All items at this point in time)
    all_items = Listing.select_all()
    return jsonify({"selected": all_items})

@app.route("/list/add/<name>/<quantity>/<price>/<location>", methods=["GET"])
def add_item(name, quantity, price,location):
    # use our Listing class add an item to the DB
    # can use a POST request if desired
    return jsonify({})

@app.route("/list/update", methods=["GET"])
def update_item():
    pass

@app.route("/list/delete", methods=["GET"])
def delete_item():
    pass

@app.route("/list/select_one/<id>", methods=["GET"])
def name(id):
    pass

#example for serving an HTML document
@app.route("/html_example", methods=["GET"])
def html_example():
    return flask.render_template("filename.html")



if __name__ == "__main__":
    app.run()
