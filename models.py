from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))


# class Cow(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     birthdate = db.Column(db.Date)
#     dam = db.Column(db.String(50))
#     sire = db.Column(db.String(50))
#     sex = db.Column(db.String(10))
#     registration_number = db.Column(db.String(20))

#     def __repr__(self):
#         return f'<Cow {self.name}>'
