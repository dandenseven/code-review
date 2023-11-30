import os
from flask_routes.routes import app
from models.listing import Listing


PATH = os.path.dirname(__file__)
Listing.dbpath = os.path.join(PATH, "data", "listings.db")

#print(Listing.select_all())


if __name__ == "__main__":
    app.run()