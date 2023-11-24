from flask import Flask, request, jsonify
from models.listing import Listing
# Client-side code would SEND a request
# This is server-side code. it's designed to RECEIVE requests

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
