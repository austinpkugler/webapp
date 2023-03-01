import os

from app import app, db, models


with app.app_context():
    db_path = os.path.join('instance', os.environ.get('DATABASE_URL').split('///')[1])
    if os.path.exists(db_path):
        os.remove(db_path)

    db.create_all()
    location1 = models.Location('General Store', 'Cityville', '123 Main St', 1234)
    db.session.add(location1)
    location2 = models.Location('Movie Theater', 'Cityville', '555 N. 2nd Ave', 1234)
    db.session.add(location2)
    location3 = models.Location('Park', 'Cityville', '982 Park Ct', 1234)
    db.session.add(location3)
    db.session.commit()
