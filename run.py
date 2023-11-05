import os
from models.listing import Listing

PATH = os.path.dirname(__file__)
#creates a path to where the database is
Listing.dbpath = os.path.join(PATH, "data", "listings.db")

print(Listing.select_all())
