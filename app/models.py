from datetime import timedelta, datetime
from app import db


class Cow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    birthdate = db.Column(db.Date)
    dam_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    sire_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    sex = db.Column(db.String(1))
    registration = db.Column(db.String(20))


class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date)
    feed_type = db.Column(db.String(50))
    amount = db.Column(db.Float)


class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date)
    drug_name = db.Column(db.String(100))
    dosage = db.Column(db.Float)
    cost = db.Column(db.Float)


class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date)
    weight = db.Column(db.Float)


class Reproduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date)
    event_type = db.Column(db.String(20))

    semen_name = db.Column(db.String(100))
    due_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    def set_due_date(self):
        if self.event_type in ('AI', 'OTB'):
            date = datetime.strptime(self.date, '%Y-%m-%d').date()
            self.due_date = (date + timedelta(days=283)).strftime('%Y-%m-%d')


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    show_date = db.Column(db.Date)
    show_name = db.Column(db.String(100))
    place = db.Column(db.Integer)
    fees = db.Column(db.Float)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date)
    note = db.Column(db.Text)
