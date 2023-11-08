import os
from models.listing import Listing

PATH = os.path.dirname(__file__)
#creates a path to where the database is
Listing.dbpath = os.path.join(PATH, "data", "listings.db")

#empty list in generated
print(Listing.select_all())
