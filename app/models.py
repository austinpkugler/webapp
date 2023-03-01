from app import db


class Location(db.Model):
    id = db.Column('location_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    zip_code = db.Column(db.Integer(), nullable=False)

    def __init__(self, name, city, address, zip_code):
        self.name = name
        self.city = city
        self.address = address
        self.zip_code = zip_code

    def __repr__(self):
        return f'Location(id={self.id}, name={self.name}, address={self.address})'
