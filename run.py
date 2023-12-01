import os
from flask_routes import app
from models import Listing


PATH = os.path.dirname(__file__)
Listing.dbpath = os.path.join(PATH, "data", "listings.db")

#print(Listing.select_all())


if __name__ == "__main__":
    app.run()