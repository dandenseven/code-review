import  sqlite3

class Listing:

    tablename = "listings"
    dbpath = "../data/listings.db"

    def __init__(self, name, quantity, price, location, pk=None):
        self.pk = pk
        self.name = name
        self.quantity = quantity
        self.price = price
        self.location = location
    
    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename} (
                        name, quantity, price, location
                        ) VALUES (?,?,?,?);"""
            values = (self.name, self.quantity, self.price, self.location)
            cursor.execute(sql, values)

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def select_all(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            # TODO: Prevents sql injection
            sql = f"""SELECT * from {cls.tablename}"""
            cursor.execute(sql)
            return cursor.fetchall()

    @classmethod
    def select_one(cls):
        pass

if __name__ == "__main__":
    listings = Listing.select_all()
    print(listings)
    new_item = Listing("name", 5, 12.99, "test location")
    new_item.insert()
