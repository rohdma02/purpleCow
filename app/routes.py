from app import app, db
from datetime import timedelta
from flask import render_template
from app.models import Cow, Feeding, Medication, Note, Reproduction, Show, Weight


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/animals/")
def animals():
    cows = Cow.query.all()
    return render_template("animals.html", cows=cows)


@app.route("/details/<id>")
def details(id):
    cow = Cow.query.get_or_404(id)
    feedings = Feeding.query.filter_by(cow_id=id).all()
    medications = Medication.query.filter_by(cow_id=id).all()
    weights = Weight.query.filter_by(cow_id=id).all()
    reproductions = Reproduction.query.filter_by(cow_id=id).all()
    shows = Show.query.filter_by(cow_id=id).all()
    notes = Note.query.filter_by(cow_id=id).all()

    return render_template("details.html",
                           cow=cow,
                           feedings=feedings,
                           medications=medications,
                           weights=weights,
                           reproductions=reproductions,
                           shows=shows,
                           notes=notes)


@app.route("/add_fake_data")
def add_fake_data():
    # Delete all existing records
    Cow.query.delete()
    Feeding.query.delete()
    Medication.query.delete()
    Weight.query.delete()
    Reproduction.query.delete()
    Show.query.delete()
    Note.query.delete()

    # Commit the changes to the database
    db.session.commit()

    # Add a fake cow
    cow = Cow(name='Bessie', birthdate='2022-01-01',
              sex='F', registration='12345')
    db.session.add(cow)
    db.session.commit()  # Commit the cow first to get its id

    # Add fake feeding record for the cow
    feeding = Feeding(cow_id=cow.id, date='2022-01-10',
                      feed_type='Hay', amount=5.0)
    db.session.add(feeding)

    # Add fake medication record for the cow
    medication = Medication(cow_id=cow.id, date='2022-01-15',
                            drug_name='Vaccine', dosage=2.0, cost=10.0)
    db.session.add(medication)

    # Add fake weight record for the cow
    weight = Weight(cow_id=cow.id, date='2022-02-01', weight=500.0)
    db.session.add(weight)

    # Add fake reproduction record for the cow
    reproduction = Reproduction(
        cow_id=cow.id, date='2022-03-01', event_type='AI', semen_name='BullA')
    str(reproduction.set_due_date())
    db.session.add(reproduction)

    # Add fake show record for the cow
    show = Show(cow_id=cow.id, show_date='2022-04-01',
                show_name='Best in Show', place=1, fees=20.0)
    db.session.add(show)

    # Add fake note for the cow
    note = Note(cow_id=cow.id, date='2022-05-01', note='This is a test note.')
    db.session.add(note)

    # Commit the changes to the database
    db.session.commit()

    return "Fake data added successfully!"
